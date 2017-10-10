# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: synse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='synse.proto',
  package='main',
  syntax='proto3',
  serialized_pb=_b('\n\x0bsynse.proto\x12\x04main\"\x1a\n\x0bReadRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\")\n\x0cWriteRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t\".\n\x0fMetainfoRequest\x12\x0c\n\x04rack\x18\x01 \x01(\t\x12\r\n\x05\x62oard\x18\x02 \x01(\t\"\x1b\n\rTransactionId\x12\n\n\x02id\x18\x01 \x01(\t\"Q\n\x0cReadResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.main.ReadingType\x12\r\n\x05value\x18\x03 \x01(\t\"\xde\x01\n\x10MetainfoResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x05 \x01(\t\x12\x10\n\x08protocol\x18\x06 \x01(\t\x12\x0c\n\x04info\x18\x07 \x01(\t\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12$\n\x08location\x18\t \x01(\x0b\x32\x12.main.MetaLocation\x12 \n\x06output\x18\n \x03(\x0b\x32\x10.main.MetaOutput\"\xe3\x01\n\rWriteResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.main.WriteResponse.WriteStatus\x12-\n\x05state\x18\x03 \x01(\x0e\x32\x1e.main.WriteResponse.WriteState\">\n\x0bWriteStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07WRITING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\"\x1f\n\nWriteState\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\".\n\x0eMetaOutputUnit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"+\n\x0fMetaOutputRange\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\"w\n\nMetaOutput\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tprecision\x18\x02 \x01(\x05\x12\"\n\x04unit\x18\x03 \x01(\x0b\x32\x14.main.MetaOutputUnit\x12$\n\x05range\x18\x04 \x01(\x0b\x32\x15.main.MetaOutputRange\";\n\x0cMetaLocation\x12\x0c\n\x04rack\x18\x01 \x01(\t\x12\r\n\x05\x62oard\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\t*\x7f\n\x0bReadingType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\x19\n\x15\x44IFFERENTIAL_PRESSURE\x10\x02\x12\x0b\n\x07\x41IRFLOW\x10\x03\x12\x0c\n\x08HUMIDITY\x10\x04\x12\r\n\tLED_STATE\x10\x05\x12\r\n\tLED_BLINK\x10\x06\x32\xf3\x01\n\x0bInternalApi\x12\x31\n\x04Read\x12\x11.main.ReadRequest\x1a\x12.main.ReadResponse\"\x00\x30\x01\x12\x32\n\x05Write\x12\x12.main.WriteRequest\x1a\x13.main.TransactionId\"\x00\x12=\n\x08Metainfo\x12\x15.main.MetainfoRequest\x1a\x16.main.MetainfoResponse\"\x00\x30\x01\x12>\n\x10TransactionCheck\x12\x13.main.TransactionId\x1a\x13.main.WriteResponse\"\x00\x62\x06proto3')
)

_READINGTYPE = _descriptor.EnumDescriptor(
  name='ReadingType',
  full_name='main.ReadingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIFFERENTIAL_PRESSURE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIRFLOW', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HUMIDITY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_STATE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_BLINK', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=982,
  serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_READINGTYPE)

ReadingType = enum_type_wrapper.EnumTypeWrapper(_READINGTYPE)
UNKNOWN = 0
TEMPERATURE = 1
DIFFERENTIAL_PRESSURE = 2
AIRFLOW = 3
HUMIDITY = 4
LED_STATE = 5
LED_BLINK = 6


_WRITERESPONSE_WRITESTATUS = _descriptor.EnumDescriptor(
  name='WriteStatus',
  full_name='main.WriteResponse.WriteStatus',
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
  serialized_start=610,
  serialized_end=672,
)
_sym_db.RegisterEnumDescriptor(_WRITERESPONSE_WRITESTATUS)

_WRITERESPONSE_WRITESTATE = _descriptor.EnumDescriptor(
  name='WriteState',
  full_name='main.WriteResponse.WriteState',
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
  serialized_start=674,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_WRITERESPONSE_WRITESTATE)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='main.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='main.ReadRequest.uid', index=0,
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
  serialized_start=21,
  serialized_end=47,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='main.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='main.WriteRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='main.WriteRequest.data', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=49,
  serialized_end=90,
)


_METAINFOREQUEST = _descriptor.Descriptor(
  name='MetainfoRequest',
  full_name='main.MetainfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rack', full_name='main.MetainfoRequest.rack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='board', full_name='main.MetainfoRequest.board', index=1,
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
  serialized_start=92,
  serialized_end=138,
)


_TRANSACTIONID = _descriptor.Descriptor(
  name='TransactionId',
  full_name='main.TransactionId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='main.TransactionId.id', index=0,
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
  serialized_start=140,
  serialized_end=167,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='main.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='main.ReadResponse.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='main.ReadResponse.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='main.ReadResponse.value', index=2,
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
  serialized_start=169,
  serialized_end=250,
)


_METAINFORESPONSE = _descriptor.Descriptor(
  name='MetainfoResponse',
  full_name='main.MetainfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='main.MetainfoResponse.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='main.MetainfoResponse.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='main.MetainfoResponse.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='main.MetainfoResponse.model', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='main.MetainfoResponse.manufacturer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='main.MetainfoResponse.protocol', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='main.MetainfoResponse.info', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='main.MetainfoResponse.comment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='main.MetainfoResponse.location', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='main.MetainfoResponse.output', index=9,
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
  serialized_start=253,
  serialized_end=475,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='main.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='main.WriteResponse.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='main.WriteResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='main.WriteResponse.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=478,
  serialized_end=705,
)


_METAOUTPUTUNIT = _descriptor.Descriptor(
  name='MetaOutputUnit',
  full_name='main.MetaOutputUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='main.MetaOutputUnit.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='main.MetaOutputUnit.symbol', index=1,
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
  serialized_start=707,
  serialized_end=753,
)


_METAOUTPUTRANGE = _descriptor.Descriptor(
  name='MetaOutputRange',
  full_name='main.MetaOutputRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='main.MetaOutputRange.min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='main.MetaOutputRange.max', index=1,
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
  serialized_start=755,
  serialized_end=798,
)


_METAOUTPUT = _descriptor.Descriptor(
  name='MetaOutput',
  full_name='main.MetaOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='main.MetaOutput.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='main.MetaOutput.precision', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='main.MetaOutput.unit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='main.MetaOutput.range', index=3,
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
  serialized_start=800,
  serialized_end=919,
)


_METALOCATION = _descriptor.Descriptor(
  name='MetaLocation',
  full_name='main.MetaLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rack', full_name='main.MetaLocation.rack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='board', full_name='main.MetaLocation.board', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='main.MetaLocation.device', index=2,
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
  serialized_start=921,
  serialized_end=980,
)

_READRESPONSE.fields_by_name['type'].enum_type = _READINGTYPE
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
DESCRIPTOR.message_types_by_name['MetainfoResponse'] = _METAINFORESPONSE
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['MetaOutputUnit'] = _METAOUTPUTUNIT
DESCRIPTOR.message_types_by_name['MetaOutputRange'] = _METAOUTPUTRANGE
DESCRIPTOR.message_types_by_name['MetaOutput'] = _METAOUTPUT
DESCRIPTOR.message_types_by_name['MetaLocation'] = _METALOCATION
DESCRIPTOR.enum_types_by_name['ReadingType'] = _READINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.WriteRequest)
  ))
_sym_db.RegisterMessage(WriteRequest)

MetainfoRequest = _reflection.GeneratedProtocolMessageType('MetainfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _METAINFOREQUEST,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetainfoRequest)
  ))
_sym_db.RegisterMessage(MetainfoRequest)

TransactionId = _reflection.GeneratedProtocolMessageType('TransactionId', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONID,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.TransactionId)
  ))
_sym_db.RegisterMessage(TransactionId)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

MetainfoResponse = _reflection.GeneratedProtocolMessageType('MetainfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _METAINFORESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetainfoResponse)
  ))
_sym_db.RegisterMessage(MetainfoResponse)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITERESPONSE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.WriteResponse)
  ))
_sym_db.RegisterMessage(WriteResponse)

MetaOutputUnit = _reflection.GeneratedProtocolMessageType('MetaOutputUnit', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUTUNIT,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetaOutputUnit)
  ))
_sym_db.RegisterMessage(MetaOutputUnit)

MetaOutputRange = _reflection.GeneratedProtocolMessageType('MetaOutputRange', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUTRANGE,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetaOutputRange)
  ))
_sym_db.RegisterMessage(MetaOutputRange)

MetaOutput = _reflection.GeneratedProtocolMessageType('MetaOutput', (_message.Message,), dict(
  DESCRIPTOR = _METAOUTPUT,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetaOutput)
  ))
_sym_db.RegisterMessage(MetaOutput)

MetaLocation = _reflection.GeneratedProtocolMessageType('MetaLocation', (_message.Message,), dict(
  DESCRIPTOR = _METALOCATION,
  __module__ = 'synse_pb2'
  # @@protoc_insertion_point(class_scope:main.MetaLocation)
  ))
_sym_db.RegisterMessage(MetaLocation)


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
          '/main.InternalApi/Read',
          request_serializer=ReadRequest.SerializeToString,
          response_deserializer=ReadResponse.FromString,
          )
      self.Write = channel.unary_unary(
          '/main.InternalApi/Write',
          request_serializer=WriteRequest.SerializeToString,
          response_deserializer=TransactionId.FromString,
          )
      self.Metainfo = channel.unary_stream(
          '/main.InternalApi/Metainfo',
          request_serializer=MetainfoRequest.SerializeToString,
          response_deserializer=MetainfoResponse.FromString,
          )
      self.TransactionCheck = channel.unary_unary(
          '/main.InternalApi/TransactionCheck',
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
            response_serializer=TransactionId.SerializeToString,
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
        'main.InternalApi', rpc_method_handlers)
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
      ('main.InternalApi', 'Metainfo'): MetainfoRequest.FromString,
      ('main.InternalApi', 'Read'): ReadRequest.FromString,
      ('main.InternalApi', 'TransactionCheck'): TransactionId.FromString,
      ('main.InternalApi', 'Write'): WriteRequest.FromString,
    }
    response_serializers = {
      ('main.InternalApi', 'Metainfo'): MetainfoResponse.SerializeToString,
      ('main.InternalApi', 'Read'): ReadResponse.SerializeToString,
      ('main.InternalApi', 'TransactionCheck'): WriteResponse.SerializeToString,
      ('main.InternalApi', 'Write'): TransactionId.SerializeToString,
    }
    method_implementations = {
      ('main.InternalApi', 'Metainfo'): face_utilities.unary_stream_inline(servicer.Metainfo),
      ('main.InternalApi', 'Read'): face_utilities.unary_stream_inline(servicer.Read),
      ('main.InternalApi', 'TransactionCheck'): face_utilities.unary_unary_inline(servicer.TransactionCheck),
      ('main.InternalApi', 'Write'): face_utilities.unary_unary_inline(servicer.Write),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_InternalApi_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('main.InternalApi', 'Metainfo'): MetainfoRequest.SerializeToString,
      ('main.InternalApi', 'Read'): ReadRequest.SerializeToString,
      ('main.InternalApi', 'TransactionCheck'): TransactionId.SerializeToString,
      ('main.InternalApi', 'Write'): WriteRequest.SerializeToString,
    }
    response_deserializers = {
      ('main.InternalApi', 'Metainfo'): MetainfoResponse.FromString,
      ('main.InternalApi', 'Read'): ReadResponse.FromString,
      ('main.InternalApi', 'TransactionCheck'): WriteResponse.FromString,
      ('main.InternalApi', 'Write'): TransactionId.FromString,
    }
    cardinalities = {
      'Metainfo': cardinality.Cardinality.UNARY_STREAM,
      'Read': cardinality.Cardinality.UNARY_STREAM,
      'TransactionCheck': cardinality.Cardinality.UNARY_UNARY,
      'Write': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'main.InternalApi', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
