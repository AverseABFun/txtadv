# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttaw.proto\x12\x03taw\x1a\x19google/protobuf/any.proto\"$\n\x04\x44ict\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\x0e\n\x06values\x18\x02 \x03(\x0c\"(\n\x08\x42oolDict\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\x0e\n\x06values\x18\x02 \x03(\x08\"\x9d\x01\n\x06Script\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1e\n\x04\x63ode\x18\x04 \x02(\x0b\x32\x10.taw.Script.Code\x1aG\n\x04\x43ode\x12\x0e\n\x06script\x18\x01 \x02(\t\x12/\n\x04type\x18\x02 \x01(\x0e\x32\x16.taw.Script.ScriptType:\tNATIVE_PY\"\x1b\n\nScriptType\x12\r\n\tNATIVE_PY\x10\x00\"g\n\x04Room\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05iname\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x02(\t\x12\x18\n\x05\x65xits\x18\x04 \x03(\x0b\x32\t.taw.Room\x12\x1a\n\x05items\x18\x05 \x03(\x0b\x32\x0b.taw.Object\"y\n\x06Object\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05sdesc\x18\x02 \x02(\t\x12\r\n\x05ldesc\x18\x03 \x02(\t\x12\x16\n\x03loc\x18\x04 \x02(\x0b\x32\t.taw.Room\x12\r\n\x05iname\x18\x05 \x02(\t\x12\x1c\n\x05\x66lags\x18\x06 \x01(\x0b\x32\r.taw.BoolDict\"w\n\x04Item\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05sdesc\x18\x02 \x02(\t\x12\r\n\x05ldesc\x18\x03 \x02(\t\x12\x16\n\x03loc\x18\x04 \x02(\x0b\x32\t.taw.Room\x12\r\n\x05iname\x18\x05 \x02(\t\x12\x1c\n\x05\x66lags\x18\x06 \x01(\x0b\x32\r.taw.BoolDict\"}\n\x05World\x12$\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x12.taw.World.Command\x12\x17\n\x04room\x18\x02 \x02(\x0b\x32\t.taw.Room\x1a\x35\n\x07\x43ommand\x12\x0f\n\x07\x61liases\x18\x01 \x03(\t\x12\x19\n\x04\x63ode\x18\x02 \x02(\x0b\x32\x0b.taw.Script\";\n\x04Save\x12\x19\n\x05world\x18\x01 \x02(\x0b\x32\n.taw.World\x12\x18\n\x05saves\x18\x02 \x01(\x0b\x32\t.taw.Dict\"]\n\x06Player\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x03loc\x18\x02 \x02(\x0b\x32\t.taw.Room\x12\x1c\n\tinventory\x18\x03 \x02(\x0b\x32\t.taw.Room\x12\x0f\n\x07\x63olored\x18\x04 \x02(\x08\"L\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x03loc\x18\x02 \x02(\x0b\x32\t.taw.Room\x12\x1c\n\tinventory\x18\x03 \x02(\x0b\x32\t.taw.Room\"S\n\x05\x45vent\x12$\n\x06target\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x12$\n\x06\x61\x63tion\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"E\n\x0fMovePlayerEvent\x12\x1b\n\x06target\x18\x01 \x02(\x0b\x32\x0b.taw.Player\x12\x15\n\x02to\x18\x02 \x02(\x0b\x32\t.taw.Room\"E\n\x0fMoveObjectEvent\x12\x1b\n\x06target\x18\x01 \x02(\x0b\x32\x0b.taw.Object\x12\x15\n\x02to\x18\x02 \x02(\x0b\x32\t.taw.Room\"A\n\rMoveItemEvent\x12\x19\n\x06target\x18\x01 \x02(\x0b\x32\t.taw.Item\x12\x15\n\x02to\x18\x02 \x02(\x0b\x32\t.taw.Room\"]\n\x0c\x41\x64\x64\x45xitEvent\x12\x19\n\x06target\x18\x01 \x02(\x0b\x32\t.taw.Room\x12\x1b\n\x03\x64ir\x18\x02 \x02(\x0e\x32\x0e.taw.Direction\x12\x15\n\x02to\x18\x03 \x02(\x0b\x32\t.taw.Room\"9\n\x0eLocalChatEvent\x12\x19\n\x06source\x18\x01 \x02(\x0b\x32\t.taw.Room\x12\x0c\n\x04mess\x18\x02 \x02(\t\"\x1f\n\x0fGlobalChatEvent\x12\x0c\n\x04mess\x18\x01 \x02(\t*G\n\tDirection\x12\t\n\x05NORTH\x10\x00\x12\t\n\x05SOUTH\x10\x01\x12\x08\n\x04\x45\x41ST\x10\x02\x12\x08\n\x04WEST\x10\x03\x12\x06\n\x02UP\x10\x04\x12\x08\n\x04\x44OWN\x10\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'taw_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DIRECTION']._serialized_start=1476
  _globals['_DIRECTION']._serialized_end=1547
  _globals['_DICT']._serialized_start=45
  _globals['_DICT']._serialized_end=81
  _globals['_BOOLDICT']._serialized_start=83
  _globals['_BOOLDICT']._serialized_end=123
  _globals['_SCRIPT']._serialized_start=126
  _globals['_SCRIPT']._serialized_end=283
  _globals['_SCRIPT_CODE']._serialized_start=183
  _globals['_SCRIPT_CODE']._serialized_end=254
  _globals['_SCRIPT_SCRIPTTYPE']._serialized_start=256
  _globals['_SCRIPT_SCRIPTTYPE']._serialized_end=283
  _globals['_ROOM']._serialized_start=285
  _globals['_ROOM']._serialized_end=388
  _globals['_OBJECT']._serialized_start=390
  _globals['_OBJECT']._serialized_end=511
  _globals['_ITEM']._serialized_start=513
  _globals['_ITEM']._serialized_end=632
  _globals['_WORLD']._serialized_start=634
  _globals['_WORLD']._serialized_end=759
  _globals['_WORLD_COMMAND']._serialized_start=706
  _globals['_WORLD_COMMAND']._serialized_end=759
  _globals['_SAVE']._serialized_start=761
  _globals['_SAVE']._serialized_end=820
  _globals['_PLAYER']._serialized_start=822
  _globals['_PLAYER']._serialized_end=915
  _globals['_ENTITY']._serialized_start=917
  _globals['_ENTITY']._serialized_end=993
  _globals['_EVENT']._serialized_start=995
  _globals['_EVENT']._serialized_end=1078
  _globals['_MOVEPLAYEREVENT']._serialized_start=1080
  _globals['_MOVEPLAYEREVENT']._serialized_end=1149
  _globals['_MOVEOBJECTEVENT']._serialized_start=1151
  _globals['_MOVEOBJECTEVENT']._serialized_end=1220
  _globals['_MOVEITEMEVENT']._serialized_start=1222
  _globals['_MOVEITEMEVENT']._serialized_end=1287
  _globals['_ADDEXITEVENT']._serialized_start=1289
  _globals['_ADDEXITEVENT']._serialized_end=1382
  _globals['_LOCALCHATEVENT']._serialized_start=1384
  _globals['_LOCALCHATEVENT']._serialized_end=1441
  _globals['_GLOBALCHATEVENT']._serialized_start=1443
  _globals['_GLOBALCHATEVENT']._serialized_end=1474
# @@protoc_insertion_point(module_scope)