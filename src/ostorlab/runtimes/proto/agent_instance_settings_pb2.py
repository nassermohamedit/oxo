# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runtimes/proto/agent_instance_settings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,runtimes/proto/agent_instance_settings.proto\x12\x17ostorlab.runtimes.proto\"0\n\x03\x41rg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x0c\"<\n\x0bPortMapping\x12\x13\n\x0bsource_port\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x01(\r\"\xfd\x03\n\x15\x41gentInstanceSettings\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0f\n\x07\x62us_url\x18\x02 \x01(\t\x12\x1a\n\x12\x62us_exchange_topic\x18\x03 \x01(\t\x12\x1a\n\x12\x62us_management_url\x18\x04 \x01(\t\x12\x11\n\tbus_vhost\x18\x05 \x01(\t\x12*\n\x04\x61rgs\x18\x06 \x03(\x0b\x32\x1c.ostorlab.runtimes.proto.Arg\x12\x13\n\x0b\x63onstraints\x18\x07 \x03(\t\x12\x0e\n\x06mounts\x18\x08 \x03(\t\x12\x16\n\x0erestart_policy\x18\t \x01(\t\x12\x11\n\tmem_limit\x18\n \x01(\x04\x12\x38\n\nopen_ports\x18\x0b \x03(\x0b\x32$.ostorlab.runtimes.proto.PortMapping\x12\x10\n\x08replicas\x18\x0c \x01(\r\x12\x18\n\x10healthcheck_host\x18\r \x01(\t\x12\x18\n\x10healthcheck_port\x18\x0e \x01(\r\x12\x11\n\tredis_url\x18\x0f \x01(\t\x12\x1d\n\x15tracing_collector_url\x18\x10 \x01(\t\x12\x0c\n\x04\x63\x61ps\x18\x11 \x03(\t\x12\x1f\n\x17\x63yclic_processing_limit\x18\x12 \x01(\r\x12\x1e\n\x16processing_depth_limit\x18\x13 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'runtimes.proto.agent_instance_settings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ARG._serialized_start=73
  _ARG._serialized_end=121
  _PORTMAPPING._serialized_start=123
  _PORTMAPPING._serialized_end=183
  _AGENTINSTANCESETTINGS._serialized_start=186
  _AGENTINSTANCESETTINGS._serialized_end=695
# @@protoc_insertion_point(module_scope)
