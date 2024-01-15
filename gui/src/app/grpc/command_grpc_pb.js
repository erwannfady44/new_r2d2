// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var command_pb = require('./command_pb.js');

function serialize_command_BatteryLevel(arg) {
  if (!(arg instanceof command_pb.BatteryLevel)) {
    throw new Error('Expected argument of type command.BatteryLevel');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_command_BatteryLevel(buffer_arg) {
  return command_pb.BatteryLevel.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_command_Empty(arg) {
  if (!(arg instanceof command_pb.Empty)) {
    throw new Error('Expected argument of type command.Empty');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_command_Empty(buffer_arg) {
  return command_pb.Empty.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_command_MotorCommand(arg) {
  if (!(arg instanceof command_pb.MotorCommand)) {
    throw new Error('Expected argument of type command.MotorCommand');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_command_MotorCommand(buffer_arg) {
  return command_pb.MotorCommand.deserializeBinary(new Uint8Array(buffer_arg));
}


var CommandService = exports.CommandService = {
  sendCommand: {
    path: '/command.Command/SendCommand',
    requestStream: false,
    responseStream: false,
    requestType: command_pb.MotorCommand,
    responseType: command_pb.Empty,
    requestSerialize: serialize_command_MotorCommand,
    requestDeserialize: deserialize_command_MotorCommand,
    responseSerialize: serialize_command_Empty,
    responseDeserialize: deserialize_command_Empty,
  },
  getBatteryLevel: {
    path: '/command.Command/GetBatteryLevel',
    requestStream: false,
    responseStream: false,
    requestType: command_pb.Empty,
    responseType: command_pb.BatteryLevel,
    requestSerialize: serialize_command_Empty,
    requestDeserialize: deserialize_command_Empty,
    responseSerialize: serialize_command_BatteryLevel,
    responseDeserialize: deserialize_command_BatteryLevel,
  },
};

exports.CommandClient = grpc.makeGenericClientConstructor(CommandService);
