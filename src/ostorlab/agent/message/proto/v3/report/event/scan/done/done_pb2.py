# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: done.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='done.proto',
  package='v3.report.event.scan.done',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\ndone.proto\x12\x19v3.report.event.scan.done\"\t\n\x07Message')
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='v3.report.event.scan.done.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'done_pb2'
  # @@protoc_insertion_point(class_scope:v3.report.event.scan.done.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
