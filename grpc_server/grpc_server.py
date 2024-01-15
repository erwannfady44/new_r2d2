import sys

import grpc
from concurrent import futures
sys.path.append('generated')
# Importez directement les modules générés
from generated.command_pb2_grpc import add_CommandServicer_to_server
from generated.command_pb2 import MotorCommand, BatteryLevel, Empty
from services.CommandService import CommandService

# from generated.command_pb2_grpc import add_CommandServicer_to_server
# from services.CommandService import CommandService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CommandServicer_to_server(CommandService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
