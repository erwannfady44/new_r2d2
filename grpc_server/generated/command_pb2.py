# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcommand.proto\x12\x07\x63ommand\"K\n\x0cMotorCommand\x12\x12\n\nleft_motor\x18\x01 \x01(\x05\x12\x13\n\x0bright_motor\x18\x02 \x01(\x05\x12\x12\n\nhead_motor\x18\x03 \x01(\x05\"P\n\x0c\x42\x61tteryLevel\x12\x14\n\x0cleft_battery\x18\x01 \x01(\x05\x12\x15\n\rright_battery\x18\x02 \x01(\x05\x12\x13\n\x0bvoltage_24v\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty2y\n\x07\x43ommand\x12\x34\n\x0bSendCommand\x12\x15.command.MotorCommand\x1a\x0e.command.Empty\x12\x38\n\x0fGetBatteryLevel\x12\x0e.command.Empty\x1a\x15.command.BatteryLevelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MOTORCOMMAND']._serialized_start=26
  _globals['_MOTORCOMMAND']._serialized_end=101
  _globals['_BATTERYLEVEL']._serialized_start=103
  _globals['_BATTERYLEVEL']._serialized_end=183
  _globals['_EMPTY']._serialized_start=185
  _globals['_EMPTY']._serialized_end=192
  _globals['_COMMAND']._serialized_start=194
  _globals['_COMMAND']._serialized_end=315
# @@protoc_insertion_point(module_scope)