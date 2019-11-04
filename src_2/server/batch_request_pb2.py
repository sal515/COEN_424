# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: batch_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='batch_request.proto',
  package='batch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x62\x61tch_request.proto\x12\x05\x62\x61tch\"\x81\x01\n\nbatch_info\x12\r\n\x05rfwId\x18\x01 \x01(\t\x12\x15\n\rbenchmarkType\x18\x02 \x01(\x05\x12\x16\n\x0eworkloadMetric\x18\x03 \x01(\x05\x12\x11\n\tbatchUnit\x18\x04 \x01(\x05\x12\x0f\n\x07\x62\x61tchId\x18\x05 \x01(\x05\x12\x11\n\tbatchSize\x18\x06 \x01(\x05\"$\n\nbatch_data\x12\x16\n\x0eresponse_batch\x18\x01 \x01(\t2;\n\x05\x62\x61tch\x12\x32\n\x08getBatch\x12\x11.batch.batch_info\x1a\x11.batch.batch_data\"\x00\x62\x06proto3')
)




_BATCH_INFO = _descriptor.Descriptor(
  name='batch_info',
  full_name='batch.batch_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rfwId', full_name='batch.batch_info.rfwId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='benchmarkType', full_name='batch.batch_info.benchmarkType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workloadMetric', full_name='batch.batch_info.workloadMetric', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchUnit', full_name='batch.batch_info.batchUnit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchId', full_name='batch.batch_info.batchId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchSize', full_name='batch.batch_info.batchSize', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=160,
)


_BATCH_DATA = _descriptor.Descriptor(
  name='batch_data',
  full_name='batch.batch_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_batch', full_name='batch.batch_data.response_batch', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['batch_info'] = _BATCH_INFO
DESCRIPTOR.message_types_by_name['batch_data'] = _BATCH_DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

batch_info = _reflection.GeneratedProtocolMessageType('batch_info', (_message.Message,), {
  'DESCRIPTOR' : _BATCH_INFO,
  '__module__' : 'batch_request_pb2'
  # @@protoc_insertion_point(class_scope:batch.batch_info)
  })
_sym_db.RegisterMessage(batch_info)

batch_data = _reflection.GeneratedProtocolMessageType('batch_data', (_message.Message,), {
  'DESCRIPTOR' : _BATCH_DATA,
  '__module__' : 'batch_request_pb2'
  # @@protoc_insertion_point(class_scope:batch.batch_data)
  })
_sym_db.RegisterMessage(batch_data)



_BATCH = _descriptor.ServiceDescriptor(
  name='batch',
  full_name='batch.batch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=200,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='getBatch',
    full_name='batch.batch.getBatch',
    index=0,
    containing_service=None,
    input_type=_BATCH_INFO,
    output_type=_BATCH_DATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BATCH)

DESCRIPTOR.services_by_name['batch'] = _BATCH

# @@protoc_insertion_point(module_scope)
