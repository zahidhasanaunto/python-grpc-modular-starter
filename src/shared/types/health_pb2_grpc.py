# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import health_pb2 as health__pb2


class HealthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckHealth = channel.unary_unary(
                '/health.HealthService/CheckHealth',
                request_serializer=health__pb2.HealthCheckDto.SerializeToString,
                response_deserializer=health__pb2.HealthCheckResponse.FromString,
                )


class HealthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckHealth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckHealth': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckHealth,
                    request_deserializer=health__pb2.HealthCheckDto.FromString,
                    response_serializer=health__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'health.HealthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HealthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckHealth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/health.HealthService/CheckHealth',
            health__pb2.HealthCheckDto.SerializeToString,
            health__pb2.HealthCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)