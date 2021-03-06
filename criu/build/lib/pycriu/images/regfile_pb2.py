# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: regfile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opts_pb2
import fown_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='regfile.proto',
  package='',
  serialized_pb=_b('\n\rregfile.proto\x1a\nopts.proto\x1a\nfown.proto\"\xb0\x01\n\x0ereg_file_entry\x12\n\n\x02id\x18\x01 \x02(\r\x12\x1f\n\x05\x66lags\x18\x02 \x02(\rB\x10\xd2?\r\x1a\x0brfile.flags\x12\x0b\n\x03pos\x18\x03 \x02(\x04\x12\x19\n\x04\x66own\x18\x05 \x02(\x0b\x32\x0b.fown_entry\x12\x0c\n\x04name\x18\x06 \x02(\t\x12\x12\n\x06mnt_id\x18\x07 \x01(\x11:\x02-1\x12\x0c\n\x04size\x18\x08 \x01(\x04\x12\x0b\n\x03\x65xt\x18\t \x01(\x08\x12\x0c\n\x04mode\x18\n \x01(\r')
  ,
  dependencies=[opts_pb2.DESCRIPTOR,fown_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REG_FILE_ENTRY = _descriptor.Descriptor(
  name='reg_file_entry',
  full_name='reg_file_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='reg_file_entry.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='reg_file_entry.flags', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\r\032\013rfile.flags'))),
    _descriptor.FieldDescriptor(
      name='pos', full_name='reg_file_entry.pos', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fown', full_name='reg_file_entry.fown', index=3,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='reg_file_entry.name', index=4,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnt_id', full_name='reg_file_entry.mnt_id', index=5,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='reg_file_entry.size', index=6,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ext', full_name='reg_file_entry.ext', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='reg_file_entry.mode', index=8,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=218,
)

_REG_FILE_ENTRY.fields_by_name['fown'].message_type = fown_pb2._FOWN_ENTRY
DESCRIPTOR.message_types_by_name['reg_file_entry'] = _REG_FILE_ENTRY

reg_file_entry = _reflection.GeneratedProtocolMessageType('reg_file_entry', (_message.Message,), dict(
  DESCRIPTOR = _REG_FILE_ENTRY,
  __module__ = 'regfile_pb2'
  # @@protoc_insertion_point(class_scope:reg_file_entry)
  ))
_sym_db.RegisterMessage(reg_file_entry)


_REG_FILE_ENTRY.fields_by_name['flags'].has_options = True
_REG_FILE_ENTRY.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\r\032\013rfile.flags'))
# @@protoc_insertion_point(module_scope)
