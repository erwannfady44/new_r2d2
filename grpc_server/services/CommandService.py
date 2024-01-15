from generated.command_pb2 import MotorCommand, BatteryLevel, Empty
from generated.command_pb2_grpc import CommandServicer


class CommandService(CommandServicer):
    def GetBatteryLevel(self, request, context):
        return BatteryLevel(left_battery=100, right_battery=100, voltage_24v=100)

    def SendCommand(self, request, context):
        print(str(request.left_motor) + " " + str(request.right_motor) + " " + str(request.head_motor))
        return Empty()
