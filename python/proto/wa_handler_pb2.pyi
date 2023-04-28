from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from proto import wa_def_pb2 as _wa_def_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageSource(_message.Message):
    __slots__ = ["chat", "sender", "is_from_me", "is_group", "broadcast_list_owner"]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    IS_FROM_ME_FIELD_NUMBER: _ClassVar[int]
    IS_GROUP_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_LIST_OWNER_FIELD_NUMBER: _ClassVar[int]
    chat: str
    sender: str
    is_from_me: bool
    is_group: bool
    broadcast_list_owner: str
    def __init__(self, chat: _Optional[str] = ..., sender: _Optional[str] = ..., is_from_me: bool = ..., is_group: bool = ..., broadcast_list_owner: _Optional[str] = ...) -> None: ...

class DeviceSentMeta(_message.Message):
    __slots__ = ["destination_jid", "phash"]
    DESTINATION_JID_FIELD_NUMBER: _ClassVar[int]
    PHASH_FIELD_NUMBER: _ClassVar[int]
    destination_jid: str
    phash: str
    def __init__(self, destination_jid: _Optional[str] = ..., phash: _Optional[str] = ...) -> None: ...

class MessageInfo(_message.Message):
    __slots__ = ["message_source", "id", "type", "push_name", "timestamp", "category", "multicast", "media_type", "verified_name", "device_sent_meta"]
    MESSAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PUSH_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SENT_META_FIELD_NUMBER: _ClassVar[int]
    message_source: MessageSource
    id: str
    type: str
    push_name: str
    timestamp: _timestamp_pb2.Timestamp
    category: str
    multicast: bool
    media_type: str
    verified_name: _wa_def_pb2.VerifiedNameCertificate
    device_sent_meta: DeviceSentMeta
    def __init__(self, message_source: _Optional[_Union[MessageSource, _Mapping]] = ..., id: _Optional[str] = ..., type: _Optional[str] = ..., push_name: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[str] = ..., multicast: bool = ..., media_type: _Optional[str] = ..., verified_name: _Optional[_Union[_wa_def_pb2.VerifiedNameCertificate, _Mapping]] = ..., device_sent_meta: _Optional[_Union[DeviceSentMeta, _Mapping]] = ...) -> None: ...

class MessageEvent(_message.Message):
    __slots__ = ["info", "message", "is_ephemeral", "is_view_once", "is_view_once_v2", "is_document_with_caption", "is_edit"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_ONCE_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_ONCE_V2_FIELD_NUMBER: _ClassVar[int]
    IS_DOCUMENT_WITH_CAPTION_FIELD_NUMBER: _ClassVar[int]
    IS_EDIT_FIELD_NUMBER: _ClassVar[int]
    info: MessageInfo
    message: _wa_def_pb2.Message
    is_ephemeral: bool
    is_view_once: bool
    is_view_once_v2: bool
    is_document_with_caption: bool
    is_edit: bool
    def __init__(self, info: _Optional[_Union[MessageInfo, _Mapping]] = ..., message: _Optional[_Union[_wa_def_pb2.Message, _Mapping]] = ..., is_ephemeral: bool = ..., is_view_once: bool = ..., is_view_once_v2: bool = ..., is_document_with_caption: bool = ..., is_edit: bool = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["uuid", "action", "recipient", "payload"]
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[Command.Action]
        SEND_MESSAGE: _ClassVar[Command.Action]
    NONE: Command.Action
    SEND_MESSAGE: Command.Action
    UUID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    action: Command.Action
    recipient: str
    payload: _any_pb2.Any
    def __init__(self, uuid: _Optional[str] = ..., action: _Optional[_Union[Command.Action, str]] = ..., recipient: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AccountContext(_message.Message):
    __slots__ = ["id", "registration_id", "platform", "business_name", "push_name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    PUSH_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    registration_id: int
    platform: str
    business_name: str
    push_name: str
    def __init__(self, id: _Optional[str] = ..., registration_id: _Optional[int] = ..., platform: _Optional[str] = ..., business_name: _Optional[str] = ..., push_name: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["uuid", "timestamp", "account_context", "message_event"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    timestamp: _timestamp_pb2.Timestamp
    account_context: AccountContext
    message_event: MessageEvent
    def __init__(self, uuid: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_context: _Optional[_Union[AccountContext, _Mapping]] = ..., message_event: _Optional[_Union[MessageEvent, _Mapping]] = ...) -> None: ...
