from datetime import datetime, timedelta
from typing import Optional, List, Type, Union

from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, relationship, backref

from ..jid import normalize_jid, JID

Base = declarative_base()


class Sender(Base):
    __tablename__ = 'senders'
    _jid = Column('jid', String(255), unique=True, primary_key=True)
    push_name = Column(String(255))
    messages = relationship('Message', back_populates='sender')
    groups_owned = relationship('Group', back_populates='owner')

    @hybrid_property
    def jid(self):
        return self._jid

    @jid.setter
    def jid(self, value):
        self._jid = normalize_jid(value)


class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(String(255), primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    chat_jid = Column(String(255))
    _sender_jid = Column('sender_jid', String(255), ForeignKey('senders.jid'))
    text = Column(String(255))
    sender = relationship('Sender', back_populates='messages')

    reply_to_id = Column(String(255), ForeignKey('messages.message_id'), nullable=True)
    replies = relationship("Message", backref=backref("reply_to", remote_side=[message_id]))

    @hybrid_property
    def sender_jid(self):
        return self._sender_jid

    @sender_jid.setter
    def sender_jid(self, value):
        self._sender_jid = normalize_jid(value)


class Group(Base):
    __tablename__ = 'groups'
    group_jid = Column(String(255), ForeignKey('messages.chat_jid'), primary_key=True)
    group_name = Column(String(255))
    group_topic = Column(String(255))
    _owner_jid = Column('owner_jid', String(255), ForeignKey('senders.jid'))
    owner = relationship('Sender', back_populates='groups_owned')
    managed = Column(Boolean, default=False)
    messages = relationship('Message')

    @hybrid_property
    def owner_jid(self):
        return self._owner_jid

    @owner_jid.setter
    def owner_jid(self, value):
        self._owner_jid = normalize_jid(value)


class ChatStore:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def delete_old_messages(self):
        one_month_ago = datetime.utcnow() - timedelta(days=30)
        self.session.query(Message).filter(Message.timestamp < one_month_ago).delete()
        self.session.commit()

    def save_message(self, message_id: str, timestamp: datetime, chat_jid: str, sender_jid: str, sender_push_name: str,
                     text: str, reply_to: Optional[str] = None):
        sender = self.get_sender(sender_jid)
        if not sender:
            sender = Sender(jid=sender_jid, push_name=sender_push_name)
            self.session.merge(sender)

        chat_message = Message(message_id=message_id, timestamp=timestamp, chat_jid=chat_jid,
                               sender_jid=sender_jid, text=text, reply_to_id=reply_to)
        self.session.merge(chat_message)
        self.session.commit()

    def save_group(self, group_jid: str, group_name: Optional[str], group_topic: Optional[str],
                   owner_jid: Optional[str]):
        owner = self.session.query(Sender).filter_by(jid=owner_jid).first()
        if not owner:
            owner = Sender(jid=owner_jid)
            self.session.add(owner)

        group = Group(group_jid=group_jid, group_name=group_name, group_topic=group_topic, owner_jid=owner_jid)
        self.session.merge(group)
        self.session.commit()

    def get_group(self, group_jid: Union[JID, str]) -> Optional[Group]:
        return self.session.query(Group).filter_by(group_jid=normalize_jid(group_jid)).first()

    def fetch_messages(self, chat_jid: str, start_time: Optional[datetime] = None,
                       end_time: Optional[datetime] = None) -> Optional[List[Type[Message]]]:
        q = self.session.query(Message).filter(Message.chat_jid == normalize_jid(chat_jid))

        if start_time:
            q = q.filter(Message.timestamp >= start_time)
        if end_time:
            q = q.filter(Message.timestamp <= end_time)

        return q.all()

    def get_sender(self, jid) -> Optional[Sender]:
        return self.session.query(Sender).filter_by(jid=normalize_jid(jid)).first()
