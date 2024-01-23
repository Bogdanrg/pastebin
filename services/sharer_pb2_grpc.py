# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sharer_pb2 as sharer__pb2


class HasherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUniqueKey = channel.unary_unary(
                '/sharer.Hasher/GetUniqueKey',
                request_serializer=sharer__pb2.GetKeyRequest.SerializeToString,
                response_deserializer=sharer__pb2.GetKeyResponse.FromString,
                )
        self.GetAccess = channel.unary_unary(
                '/sharer.Hasher/GetAccess',
                request_serializer=sharer__pb2.GetAccessRequest.SerializeToString,
                response_deserializer=sharer__pb2.GetAccessResponse.FromString,
                )


class HasherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUniqueKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HasherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUniqueKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUniqueKey,
                    request_deserializer=sharer__pb2.GetKeyRequest.FromString,
                    response_serializer=sharer__pb2.GetKeyResponse.SerializeToString,
            ),
            'GetAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccess,
                    request_deserializer=sharer__pb2.GetAccessRequest.FromString,
                    response_serializer=sharer__pb2.GetAccessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sharer.Hasher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hasher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUniqueKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sharer.Hasher/GetUniqueKey',
            sharer__pb2.GetKeyRequest.SerializeToString,
            sharer__pb2.GetKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sharer.Hasher/GetAccess',
            sharer__pb2.GetAccessRequest.SerializeToString,
            sharer__pb2.GetAccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
