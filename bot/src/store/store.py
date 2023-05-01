from datetime import datetime, timedelta, timezone
from typing import Optional, List, Type, Union

from loguru import logger
from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

from ..jid import normalize_jid, JID, parse_jid

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
    message_id = Column(String(255), primary_key=True, unique=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    _chat_jid = Column('chat_jid', String(255))
    _sender_jid = Column('sender_jid', String(255), ForeignKey('senders.jid'))
    group_jid = Column('group_jid', String(255), ForeignKey('groups.group_jid'), nullable=True)
    text = Column(String(255))

    sender = relationship('Sender', back_populates='messages')
    # group = relationship('Group', back_populates='messages')

    reply_to_id = Column(String(255), ForeignKey('messages.message_id'), nullable=True)
    replies = relationship("Message", backref=backref("reply_to", remote_side=[message_id]))

    @hybrid_property
    def sender_jid(self):
        return self._sender_jid

    @sender_jid.setter
    def sender_jid(self, value):
        self._sender_jid = normalize_jid(value)

    @hybrid_property
    def chat_jid(self):
        return self._chat_jid

    @chat_jid.setter
    def chat_jid(self, value):
        jid, err = parse_jid(value)
        if err:
            logger.error(f"Invalid JID: {value}")
            self._chat_jid = value
            return

        self._chat_jid = str(jid.to_non_ad())
        if jid.is_group():
            self._group_jid = jid

    @hybrid_property
    def group_jid(self):
        return self._group_jid

    @group_jid.setter
    def group_jid(self, value):
        self._group_jid = normalize_jid(value)


class Group(Base):
    __tablename__ = 'groups'
    group_jid = Column(String(255), primary_key=True, unique=True)
    group_name = Column(String(255))
    group_topic = Column(String(255))
    _owner_jid = Column('owner_jid', String(255), ForeignKey('senders.jid'))
    owner = relationship('Sender', back_populates='groups_owned')
    managed = Column(Boolean, default=False)
    # messages = relationship('Message', back_populates='group')

    @hybrid_property
    def owner_jid(self):
        return self._owner_jid

    @owner_jid.setter
    def owner_jid(self, value):
        self._owner_jid = normalize_jid(value)


class ChatStore:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.session_maker = sessionmaker(bind=self.engine, autoflush=False)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def delete_old_messages(self):
        session = scoped_session(self.session_maker)

        one_month_ago = datetime.utcnow() - timedelta(days=30)
        session.query(Message).filter(Message.timestamp < one_month_ago).delete()
        session.commit()

    def save_message(self, message_id: str, timestamp: datetime, chat_jid: str, sender_jid: str, sender_push_name: str,
                     text: str, reply_to: Optional[str] = None):
        sender = self.get_sender(sender_jid)
        session = scoped_session(self.session_maker)

        if not sender:
            sender = Sender(jid=sender_jid, push_name=sender_push_name)
            self.upsert(session, sender)

        if reply_to == '':
            reply_to = None
        chat_message = Message(message_id=message_id, timestamp=timestamp.astimezone(timezone.utc),
                               chat_jid=chat_jid, sender_jid=sender_jid, text=text, reply_to_id=reply_to)
        self.upsert(session, chat_message)
        session.commit()

    def save_group(self, group_jid: str, group_name: Optional[str], group_topic: Optional[str],
                   owner_jid: Optional[str]):
        session = scoped_session(self.session_maker)

        owner = session.query(Sender).filter_by(jid=owner_jid).first()
        if not owner:
            owner = Sender(jid=owner_jid)
            self.upsert(session, owner)

        group = Group(group_jid=group_jid, group_name=group_name, group_topic=group_topic, owner_jid=owner_jid)
        self.upsert(session, group)
        session.commit()

    def get_group(self, group_jid: Union[JID, str]) -> Optional[Group]:
        return scoped_session(self.session_maker). \
            query(Group).filter_by(group_jid=normalize_jid(group_jid)).first()

    def fetch_messages(self, chat_jid: str, start_time: Optional[datetime] = None,
                       end_time: Optional[datetime] = None) -> Optional[List[Type[Message]]]:
        session = scoped_session(self.session_maker)

        q = session.query(Message).filter(Message.chat_jid == normalize_jid(chat_jid))

        if start_time:
            q = q.filter(Message.timestamp >= start_time.astimezone(timezone.utc))
        if end_time:
            q = q.filter(Message.timestamp <= end_time.astimezone(timezone.utc))

        return q.all()

    def get_sender(self, jid) -> Optional[Sender]:
        return scoped_session(self.session_maker).query(Sender).filter_by(jid=normalize_jid(jid)).first()

    @staticmethod
    def upsert(session, entity: Base):
        pkeys, vals = {}, {}
        for f in entity.__table__.columns:
            (pkeys if f.primary_key else vals)[f.name] = getattr(entity, f.name)
        stmt = insert(entity.__table__).values(**{**pkeys, **vals})
        stmt = stmt.on_conflict_do_update(index_elements=pkeys.keys(),set_={c.name: c for c in stmt.excluded if c.name not in pkeys})
        session.execute(stmt)
