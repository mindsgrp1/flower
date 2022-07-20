"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.fleet_pb2
import grpc

class FleetAPIStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    GetTasks: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.GetTasksRequest,
        flwr.proto.fleet_pb2.GetTasksResponse]
    """Get one or more tasks"""

    CreateResults: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fleet_pb2.CreateResultsRequest,
        flwr.proto.fleet_pb2.CreateResultsResponse]
    """Get results"""


class FleetAPIServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetTasks(self,
        request: flwr.proto.fleet_pb2.GetTasksRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.fleet_pb2.GetTasksResponse:
        """Get one or more tasks"""
        pass

    @abc.abstractmethod
    def CreateResults(self,
        request: flwr.proto.fleet_pb2.CreateResultsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.fleet_pb2.CreateResultsResponse:
        """Get results"""
        pass


def add_FleetAPIServicer_to_server(servicer: FleetAPIServicer, server: grpc.Server) -> None: ...
