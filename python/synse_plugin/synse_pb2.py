# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: synse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='synse.proto',
  package='synse',
  syntax='proto3',
  serialized_pb=_b('\n\x0bsynse.proto\x12\x05synse\"\x1a\n\x0bReadRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\";\n\x0cWriteRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x1e\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x10.synse.WriteData\".\n\x0fMetainfoRequest\x12\x0c\n\x04rack\x18\x01 \x01(\t\x12\r\n\x05\x62oard\x18\x02 \x01(\t\"\x1b\n\rTransactionId\x12\n\n\x02id\x18\x01 \x01(\t\">\n\x0cReadResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x92\x01\n\x0cTransactions\x12;\n\x0ctransactions\x18\x01 \x03(\x0b\x32%.synse.Transactions.TransactionsEntry\x1a\x45\n\x11TransactionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.synse.WriteData:\x02\x38\x01\"\xe0\x01\n\x10MetainfoResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x05 \x01(\t\x12\x10\n\x08protocol\x18\x06 \x01(\t\x12\x0c\n\x04info\x18\x07 \x01(\t\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12%\n\x08location\x18\t \x01(\x0b\x32\x13.synse.MetaLocation\x12!\n\x06output\x18\n \x03(\x0b\x32\x11.synse.MetaOutput\"\x85\x02\n\rWriteResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\t\x12\x0f\n\x07updated\x18\x02 \x01(\t\x12\x30\n\x06status\x18\x03 \x01(\x0e\x32 .synse.WriteResponse.WriteStatus\x12.\n\x05state\x18\x04 \x01(\x0e\x32\x1f.synse.WriteResponse.WriteState\x12\x0f\n\x07message\x18\x05 \x01(\t\">\n\x0bWriteStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07WRITING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\"\x1f\n\nWriteState\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"(\n\tWriteData\x12\x0b\n\x03raw\x18\x01 \x03(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\".\n\x0eMetaOutputUnit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"+\n\x0fMetaOutputRange\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\"y\n\nMetaOutput\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tprecision\x18\x02 \x01(\x05\x12#\n\x04unit\x18\x03 \x01(\x0b\x32\x15.synse.MetaOutputUnit\x12%\n\x05range\x18\x04 \x01(\x0b\x32\x16.synse.MetaOutputRange\"+\n\x0cMetaLocation\x12\x0c\n\x04rack\x18\x01 \x01(\t\x12\r\n\x05\x62oard\x18\x02 \x01(\t2\xfa\x01\n\x0bInternalApi\x12\x33\n\x04Read\x12\x12.synse.ReadRequest\x1a\x13.synse.ReadResponse\"\x00\x30\x01\x12\x33\n\x05Write\x12\x13.synse.WriteRequest\x1a\x13.synse.Transactions\"\x00\x12?\n\x08Metainfo\x12\x16.synse.MetainfoRequest\x1a\x17.synse.MetainfoResponse\"\x00\x30\x01\x12@\n\x10TransactionCheck\x12\x14.synse.TransactionId\x1a\x14.synse.WriteResponse\"\x00\x62\x06proto3')
)



_WRITERESPONSE_WRITESTATUS = _descriptor.EnumDescriptor(
  name='WriteStatus',
  full_name='synse.WriteResponse.WriteStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=795,
  serialized_end=857,
)
_sym_db.RegisterEnumDescriptor(_WRITERESPONSE_WRITESTATUS)

_WRITERESPONSE_WRITESTATE = _descriptor.EnumDescriptor(
  name='WriteState',
  full_name='synse.WriteResponse.WriteState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=859,
  serialized_end=890,
)
_sym_db.RegisterEnumDescriptor(_WRITERESPONSE_WRITESTATE)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='synse.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='synse.ReadRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=48,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='synse.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='synse.WriteRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='synse.WriteRequest.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=109,
)


_METAINFOREQUEST = _descriptor.Descriptor(
  name='MetainfoRequest',
  full_name='synse.MetainfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rack', full_name='synse.MetainfoRequest.rack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='board', full_name='synse.MetainfoRequest.board', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=157,
)


_TRANSACTIONID = _descriptor.Descriptor(
  name='TransactionId',
  full_name='synse.TransactionId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='synse.TransactionId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=186,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='synse.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='synse.ReadResponse.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='synse.ReadResponse.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='synse.ReadResponse.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=250,
)


_TRANSACTIONS_TRANSACTIONSENTRY = _descriptor.Descriptor(
  name='TransactionsEntry',
  full_name='synse.Transactions.TransactionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='synse.Transactions.TransactionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='synse.Transactions.TransactionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=399,
)

_TRANSACTIONS = _descriptor.Descriptor(
  name='Transactions',
  full_name='synse.Transactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='synse.Transactions.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONS_TRANSACTIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=399,
)


_METAINFORESPONSE = _descriptor.Descriptor(
  name='MetainfoResponse',
  full_name='synse.MetainfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='synse.MetainfoResponse.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='synse.MetainfoResponse.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='synse.MetainfoResponse.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='synse.MetainfoResponse.model', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='synse.MetainfoResponse.manufacturer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='synse.MetainfoResponse.protocol', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='synse.MetainfoResponse.info', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='synse.MetainfoResponse.comment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='synse.MetainfoResponse.location', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='synse.MetainfoResponse.output', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=626,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='synse.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='synse.WriteResponse.created', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='synse.WriteResponse.updated', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='synse.WriteResponse.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='synse.WriteResponse.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='synse.WriteResponse.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WRITERESPONSE_WRITESTATUS,
    _WRITERESPONSE_WRITESTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=629,
  serialized_end=890,
)


_WRITEDATA = _descriptor.Descriptor(
  name='WriteData',
  full_name='synse.WriteData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw', full_name='synse.WriteData.raw', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='synse.WriteData.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=932,
)


_METAOUTPUTUNIT = _descriptor.Descriptor(
  name='MetaOutputUnit',
  full_name='synse.MetaOutputUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='synse.MetaOutputUnit.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='synse.MetaOutputUnit.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=980,
)


_METAOUTPUTRANGE = _descriptor.Descriptor(
  name='MetaOutputRange',
  full_name='synse.MetaOutputRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='synse.MetaOutputRange.min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='synse.MetaOutputRange.max', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=982,
  serialized_end=1025,
)


_METAOUTPUT = _descriptor.Descriptor(
  name='MetaOutput',
  full_name='synse.MetaOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='synse.MetaOutput.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='synse.MetaOutput.precision', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='synse.MetaOutput.unit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='synse.MetaOutput.range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1027,
  serialized_end=1148,
)


_METALOCATION = _descriptor.Descriptor(
  name='MetaLocation',
  full_name='synse.MetaLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rack', full_name='synse.MetaLocation.rack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='board', full_name='synse.MetaLocation.board', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1193,
)

_WRITEREQUEST.fields_by_name['data'].message_type = _WRITEDATA
_TRANSACTIONS_TRANSACTIONSENTRY.fields_by_name['value'].message_type = _WRITEDATA
_TRANSACTIONS_TRANSACTIONSENTRY.containing_type = _TRANSACTIONS
_TRANSACTIONS.fields_by_name['transactions'].message_type = _TRANSACTIONS_TRANSACTIONSENTRY
_METAINFORESPONSE.fields_by_name['location'].message_type = _METALOCATION
_METAINFORESPONSE.fields_by_name['output'].message_type = _METAOUTPUT
_WRITERESPONSE.fields_by_name['status'].enum_type = _WRITERESPONSE_WRITESTATUS
_WRITERESPONSE.fields_by_name['state'].enum_type = _WRITERESPONSE_WRITESTATE
_WRITERESPONSE_WRITESTATUS.containing_type = _WRITERESPONSE
_WRITERESPONSE_WRITESTATE.containing_type = _WRITERESPONSE
_METAOUTPUT.fields_by_name['unit'].message_type = _METAOUTPUTUNIT
_METAOUTPUT.fields_by_name['range'].message_type = _METAOUTPUTRANGE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['MetainfoRequest'] = _METAINFOREQUEST
DESCRIPTOR.message_types_by_name['TransactionId'] = _TRANSACTIONID
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['Transactions'] = _TRANSACTIONS
DESCRIPTOR.message_types_by_name['MetainfoResponse'] = _METAINFORESPONSE
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['WriteData'] = _WRITEDATA
DESCRIPTOR.message_types_by_name['MetaOutputUnit'] = _METAOUTPUTUNIT
DESCRIPTOR.message_types_by_name['MetaOutputRange'] = _METAOUTPUTRANGE
DESCRIPTOR.message_types_by_name['MetaOutput'] = _METAOUTPUT
DESCRIPTOR.message_types_by_name['MetaLocation'] = _METALOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.WriteRequest)
  ))
_sym_db.RegisterMessage(WriteRequest)

MetainfoRequest = _reflection.GeneratedProtocolMessageType('MetainfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _METAINFOREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetainfoRequest)
  ))
_sym_db.RegisterMessage(MetainfoRequest)

TransactionId = _reflection.GeneratedProtocolMessageType('TransactionId', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONID,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.TransactionId)
  ))
_sym_db.RegisterMessage(TransactionId)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

Transactions = _reflection.GeneratedProtocolMessageType('Transactions', (_message.Message,), dict(

  TransactionsEntry = _reflection.GeneratedProtocolMessageType('TransactionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _TRANSACTIONS_TRANSACTIONSENTRY,
    __module__ = 'synse_pb2'
    # @@protoc_insertion_point(class_scope:synse.Transactions.TransactionsEntry)
    ))
  ,
  DESCRIPTOR = _TRANSACTIONS,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.Transactions)
  ))
_sym_db.RegisterMessage(Transactions)
_sym_db.RegisterMessage(Transactions.TransactionsEntry)

MetainfoResponse = _reflection.GeneratedProtocolMessageType('MetainfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _METAINFORESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetainfoResponse)
  ))
_sym_db.RegisterMessage(MetainfoResponse)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITERESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.WriteResponse)
  ))
_sym_db.RegisterMessage(WriteResponse)

WriteData = _reflection.GeneratedProtocolMessageType('WriteData', (_message.Message,), dict(
  DESCRIPTOR = _WRITEDATA,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.WriteData)
  ))
_sym_db.RegisterMessage(WriteData)

MetaOutputUnit = _reflection.GeneratedProtocolMessageType('MetaOutputUnit', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUTUNIT,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetaOutputUnit)
  ))
_sym_db.RegisterMessage(MetaOutputUnit)

MetaOutputRange = _reflection.GeneratedProtocolMessageType('MetaOutputRange', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUTRANGE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetaOutputRange)
  ))
_sym_db.RegisterMessage(MetaOutputRange)

MetaOutput = _reflection.GeneratedProtocolMessageType('MetaOutput', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUT,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetaOutput)
  ))
_sym_db.RegisterMessage(MetaOutput)

MetaLocation = _reflection.GeneratedProtocolMessageType('MetaLocation', (_message.Message,), dict(
  DESCRIPTOR = _METALOCATION,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:synse.MetaLocation)
  ))
_sym_db.RegisterMessage(MetaLocation)


_TRANSACTIONS_TRANSACTIONSENTRY.has_options = True
_TRANSACTIONS_TRANSACTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class InternalApiStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Read = channel.unary_stream(
          '/synse.InternalApi/Read',
          request_serializer=ReadRequest.SerializeToString,
          response_deserializer=ReadResponse.FromString,
          )
      self.Write = channel.unary_unary(
          '/synse.InternalApi/Write',
          request_serializer=WriteRequest.SerializeToString,
          response_deserializer=Transactions.FromString,
          )
      self.Metainfo = channel.unary_stream(
          '/synse.InternalApi/Metainfo',
          request_serializer=MetainfoRequest.SerializeToString,
          response_deserializer=MetainfoResponse.FromString,
          )
      self.TransactionCheck = channel.unary_unary(
          '/synse.InternalApi/TransactionCheck',
          request_serializer=TransactionId.SerializeToString,
          response_deserializer=WriteResponse.FromString,
          )


  class InternalApiServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Read(self, request, context):
      """Read from the specified device(s).
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
      """Write to the specified device(s).
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Metainfo(self, request, context):
      """Get the metainformation from the background process that describes
      all of the available devices which that process owns
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def TransactionCheck(self, request, context):
      """Check on the state of a write transaction.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_InternalApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Read': grpc.unary_stream_rpc_method_handler(
            servicer.Read,
            request_deserializer=ReadRequest.FromString,
            response_serializer=ReadResponse.SerializeToString,
        ),
        'Write': grpc.unary_unary_rpc_method_handler(
            servicer.Write,
            request_deserializer=WriteRequest.FromString,
            response_serializer=Transactions.SerializeToString,
        ),
        'Metainfo': grpc.unary_stream_rpc_method_handler(
            servicer.Metainfo,
            request_deserializer=MetainfoRequest.FromString,
            response_serializer=MetainfoResponse.SerializeToString,
        ),
        'TransactionCheck': grpc.unary_unary_rpc_method_handler(
            servicer.TransactionCheck,
            request_deserializer=TransactionId.FromString,
            response_serializer=WriteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'synse.InternalApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaInternalApiServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Read(self, request, context):
      """Read from the specified device(s).
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Write(self, request, context):
      """Write to the specified device(s).
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Metainfo(self, request, context):
      """Get the metainformation from the background process that describes
      all of the available devices which that process owns
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def TransactionCheck(self, request, context):
      """Check on the state of a write transaction.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaInternalApiStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Read(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Read from the specified device(s).
      """
      raise NotImplementedError()
    def Write(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Write to the specified device(s).
      """
      raise NotImplementedError()
    Write.future = None
    def Metainfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Get the metainformation from the background process that describes
      all of the available devices which that process owns
      """
      raise NotImplementedError()
    def TransactionCheck(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Check on the state of a write transaction.
      """
      raise NotImplementedError()
    TransactionCheck.future = None


  def beta_create_InternalApi_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('synse.InternalApi', 'Metainfo'): MetainfoRequest.FromString,
      ('synse.InternalApi', 'Read'): ReadRequest.FromString,
      ('synse.InternalApi', 'TransactionCheck'): TransactionId.FromString,
      ('synse.InternalApi', 'Write'): WriteRequest.FromString,
    }
    response_serializers = {
      ('synse.InternalApi', 'Metainfo'): MetainfoResponse.SerializeToString,
      ('synse.InternalApi', 'Read'): ReadResponse.SerializeToString,
      ('synse.InternalApi', 'TransactionCheck'): WriteResponse.SerializeToString,
      ('synse.InternalApi', 'Write'): Transactions.SerializeToString,
    }
    method_implementations = {
      ('synse.InternalApi', 'Metainfo'): face_utilities.unary_stream_inline(servicer.Metainfo),
      ('synse.InternalApi', 'Read'): face_utilities.unary_stream_inline(servicer.Read),
      ('synse.InternalApi', 'TransactionCheck'): face_utilities.unary_unary_inline(servicer.TransactionCheck),
      ('synse.InternalApi', 'Write'): face_utilities.unary_unary_inline(servicer.Write),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_InternalApi_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('synse.InternalApi', 'Metainfo'): MetainfoRequest.SerializeToString,
      ('synse.InternalApi', 'Read'): ReadRequest.SerializeToString,
      ('synse.InternalApi', 'TransactionCheck'): TransactionId.SerializeToString,
      ('synse.InternalApi', 'Write'): WriteRequest.SerializeToString,
    }
    response_deserializers = {
      ('synse.InternalApi', 'Metainfo'): MetainfoResponse.FromString,
      ('synse.InternalApi', 'Read'): ReadResponse.FromString,
      ('synse.InternalApi', 'TransactionCheck'): WriteResponse.FromString,
      ('synse.InternalApi', 'Write'): Transactions.FromString,
    }
    cardinalities = {
      'Metainfo': cardinality.Cardinality.UNARY_STREAM,
      'Read': cardinality.Cardinality.UNARY_STREAM,
      'TransactionCheck': cardinality.Cardinality.UNARY_UNARY,
      'Write': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'synse.InternalApi', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
