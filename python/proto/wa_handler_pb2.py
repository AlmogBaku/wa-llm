# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/wa-handler.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto import wa_def_pb2 as proto_dot_wa__def__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proto/wa-handler.proto\x12\x05proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12proto/wa-def.proto\"\xa6\x01\n\rMessageSource\x12\x12\n\x04\x63hat\x18\x01 \x01(\tR\x04\x63hat\x12\x16\n\x06sender\x18\x02 \x01(\tR\x06sender\x12\x1c\n\nis_from_me\x18\x03 \x01(\x08R\x08isFromMe\x12\x19\n\x08is_group\x18\x04 \x01(\x08R\x07isGroup\x12\x30\n\x14\x62roadcast_list_owner\x18\x05 \x01(\tR\x12\x62roadcastListOwner\"O\n\x0e\x44\x65viceSentMeta\x12\'\n\x0f\x64\x65stination_jid\x18\x01 \x01(\tR\x0e\x64\x65stinationJid\x12\x14\n\x05phash\x18\x02 \x01(\tR\x05phash\"\xa4\x03\n\x0bMessageInfo\x12;\n\x0emessage_source\x18\x01 \x01(\x0b\x32\x14.proto.MessageSourceR\rmessageSource\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x1b\n\tpush_name\x18\x04 \x01(\tR\x08pushName\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x1a\n\x08\x63\x61tegory\x18\x06 \x01(\tR\x08\x63\x61tegory\x12\x1c\n\tmulticast\x18\x07 \x01(\x08R\tmulticast\x12\x1d\n\nmedia_type\x18\x08 \x01(\tR\tmediaType\x12\x43\n\rverified_name\x18\t \x01(\x0b\x32\x1e.proto.VerifiedNameCertificateR\x0cverifiedName\x12?\n\x10\x64\x65vice_sent_meta\x18\n \x01(\x0b\x32\x15.proto.DeviceSentMetaR\x0e\x64\x65viceSentMeta\"\x9e\x02\n\x0cMessageEvent\x12&\n\x04info\x18\x02 \x01(\x0b\x32\x12.proto.MessageInfoR\x04info\x12(\n\x07message\x18\x03 \x01(\x0b\x32\x0e.proto.MessageR\x07message\x12!\n\x0cis_ephemeral\x18\x04 \x01(\x08R\x0bisEphemeral\x12 \n\x0cis_view_once\x18\x05 \x01(\x08R\nisViewOnce\x12%\n\x0fis_view_once_v2\x18\x06 \x01(\x08R\x0cisViewOnceV2\x12\x37\n\x18is_document_with_caption\x18\x07 \x01(\x08R\x15isDocumentWithCaption\x12\x17\n\x07is_edit\x18\x08 \x01(\x08R\x06isEdit\"\xc0\x01\n\x07\x43ommand\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12-\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x15.proto.Command.ActionR\x06\x61\x63tion\x12\x1c\n\trecipient\x18\x03 \x01(\tR\trecipient\x12.\n\x07payload\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyR\x07payload\"$\n\x06\x41\x63tion\x12\x08\n\x04NONE\x10\x00\x12\x10\n\x0cSEND_MESSAGE\x10\x01\"\xa7\x01\n\x0e\x41\x63\x63ountContext\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0fregistration_id\x18\x02 \x01(\rR\x0eregistrationId\x12\x1a\n\x08platform\x18\x03 \x01(\tR\x08platform\x12#\n\rbusiness_name\x18\x04 \x01(\tR\x0c\x62usinessName\x12\x1b\n\tpush_name\x18\x05 \x01(\tR\x08pushName\"\xda\x01\n\x05\x45vent\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12>\n\x0f\x61\x63\x63ount_context\x18\x03 \x01(\x0b\x32\x15.proto.AccountContextR\x0e\x61\x63\x63ountContext\x12:\n\rmessage_event\x18\x04 \x01(\x0b\x32\x13.proto.MessageEventH\x00R\x0cmessageEventB\x07\n\x05\x65vent25\n\x07Handler\x12*\n\x06Handle\x12\x0c.proto.Event\x1a\x0e.proto.Command(\x01\x30\x01\x42q\n\tcom.protoB\x0eWaHandlerProtoP\x01Z go.mau.fi/whatsmeow/binary/proto\xa2\x02\x03PXX\xaa\x02\x05Proto\xca\x02\x05Proto\xe2\x02\x11Proto\\GPBMetadata\xea\x02\x05Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.wa_handler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\tcom.protoB\016WaHandlerProtoP\001Z go.mau.fi/whatsmeow/binary/proto\242\002\003PXX\252\002\005Proto\312\002\005Proto\342\002\021Proto\\GPBMetadata\352\002\005Proto'
  _globals['_MESSAGESOURCE']._serialized_start=114
  _globals['_MESSAGESOURCE']._serialized_end=280
  _globals['_DEVICESENTMETA']._serialized_start=282
  _globals['_DEVICESENTMETA']._serialized_end=361
  _globals['_MESSAGEINFO']._serialized_start=364
  _globals['_MESSAGEINFO']._serialized_end=784
  _globals['_MESSAGEEVENT']._serialized_start=787
  _globals['_MESSAGEEVENT']._serialized_end=1073
  _globals['_COMMAND']._serialized_start=1076
  _globals['_COMMAND']._serialized_end=1268
  _globals['_COMMAND_ACTION']._serialized_start=1232
  _globals['_COMMAND_ACTION']._serialized_end=1268
  _globals['_ACCOUNTCONTEXT']._serialized_start=1271
  _globals['_ACCOUNTCONTEXT']._serialized_end=1438
  _globals['_EVENT']._serialized_start=1441
  _globals['_EVENT']._serialized_end=1659
  _globals['_HANDLER']._serialized_start=1661
  _globals['_HANDLER']._serialized_end=1714
# @@protoc_insertion_point(module_scope)
