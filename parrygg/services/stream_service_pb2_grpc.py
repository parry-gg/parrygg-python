"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ..services import stream_service_pb2 as services_dot_stream__service__pb2
GRPC_GENERATED_VERSION = '1.71.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in services/stream_service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class StreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStream = channel.unary_unary('/parrygg.services.StreamService/CreateStream', request_serializer=services_dot_stream__service__pb2.CreateStreamRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.CreateStreamResponse.FromString, _registered_method=True)
        self.UpdateStream = channel.unary_unary('/parrygg.services.StreamService/UpdateStream', request_serializer=services_dot_stream__service__pb2.UpdateStreamRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.UpdateStreamResponse.FromString, _registered_method=True)
        self.DeleteStream = channel.unary_unary('/parrygg.services.StreamService/DeleteStream', request_serializer=services_dot_stream__service__pb2.DeleteStreamRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.DeleteStreamResponse.FromString, _registered_method=True)
        self.GetTournamentStreams = channel.unary_unary('/parrygg.services.StreamService/GetTournamentStreams', request_serializer=services_dot_stream__service__pb2.GetTournamentStreamsRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.GetTournamentStreamsResponse.FromString, _registered_method=True)
        self.GetStreamQueue = channel.unary_unary('/parrygg.services.StreamService/GetStreamQueue', request_serializer=services_dot_stream__service__pb2.GetStreamQueueRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.GetStreamQueueResponse.FromString, _registered_method=True)
        self.AddMatchToStreamQueue = channel.unary_unary('/parrygg.services.StreamService/AddMatchToStreamQueue', request_serializer=services_dot_stream__service__pb2.AddMatchToStreamQueueRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.AddMatchToStreamQueueResponse.FromString, _registered_method=True)
        self.RemoveMatchFromStreamQueue = channel.unary_unary('/parrygg.services.StreamService/RemoveMatchFromStreamQueue', request_serializer=services_dot_stream__service__pb2.RemoveMatchFromStreamQueueRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.RemoveMatchFromStreamQueueResponse.FromString, _registered_method=True)
        self.ReorderStreamQueueEntry = channel.unary_unary('/parrygg.services.StreamService/ReorderStreamQueueEntry', request_serializer=services_dot_stream__service__pb2.ReorderStreamQueueEntryRequest.SerializeToString, response_deserializer=services_dot_stream__service__pb2.ReorderStreamQueueEntryResponse.FromString, _registered_method=True)

class StreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTournamentStreams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStreamQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMatchToStreamQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveMatchFromStreamQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReorderStreamQueueEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_StreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateStream': grpc.unary_unary_rpc_method_handler(servicer.CreateStream, request_deserializer=services_dot_stream__service__pb2.CreateStreamRequest.FromString, response_serializer=services_dot_stream__service__pb2.CreateStreamResponse.SerializeToString), 'UpdateStream': grpc.unary_unary_rpc_method_handler(servicer.UpdateStream, request_deserializer=services_dot_stream__service__pb2.UpdateStreamRequest.FromString, response_serializer=services_dot_stream__service__pb2.UpdateStreamResponse.SerializeToString), 'DeleteStream': grpc.unary_unary_rpc_method_handler(servicer.DeleteStream, request_deserializer=services_dot_stream__service__pb2.DeleteStreamRequest.FromString, response_serializer=services_dot_stream__service__pb2.DeleteStreamResponse.SerializeToString), 'GetTournamentStreams': grpc.unary_unary_rpc_method_handler(servicer.GetTournamentStreams, request_deserializer=services_dot_stream__service__pb2.GetTournamentStreamsRequest.FromString, response_serializer=services_dot_stream__service__pb2.GetTournamentStreamsResponse.SerializeToString), 'GetStreamQueue': grpc.unary_unary_rpc_method_handler(servicer.GetStreamQueue, request_deserializer=services_dot_stream__service__pb2.GetStreamQueueRequest.FromString, response_serializer=services_dot_stream__service__pb2.GetStreamQueueResponse.SerializeToString), 'AddMatchToStreamQueue': grpc.unary_unary_rpc_method_handler(servicer.AddMatchToStreamQueue, request_deserializer=services_dot_stream__service__pb2.AddMatchToStreamQueueRequest.FromString, response_serializer=services_dot_stream__service__pb2.AddMatchToStreamQueueResponse.SerializeToString), 'RemoveMatchFromStreamQueue': grpc.unary_unary_rpc_method_handler(servicer.RemoveMatchFromStreamQueue, request_deserializer=services_dot_stream__service__pb2.RemoveMatchFromStreamQueueRequest.FromString, response_serializer=services_dot_stream__service__pb2.RemoveMatchFromStreamQueueResponse.SerializeToString), 'ReorderStreamQueueEntry': grpc.unary_unary_rpc_method_handler(servicer.ReorderStreamQueueEntry, request_deserializer=services_dot_stream__service__pb2.ReorderStreamQueueEntryRequest.FromString, response_serializer=services_dot_stream__service__pb2.ReorderStreamQueueEntryResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('parrygg.services.StreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('parrygg.services.StreamService', rpc_method_handlers)

class StreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/CreateStream', services_dot_stream__service__pb2.CreateStreamRequest.SerializeToString, services_dot_stream__service__pb2.CreateStreamResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/UpdateStream', services_dot_stream__service__pb2.UpdateStreamRequest.SerializeToString, services_dot_stream__service__pb2.UpdateStreamResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/DeleteStream', services_dot_stream__service__pb2.DeleteStreamRequest.SerializeToString, services_dot_stream__service__pb2.DeleteStreamResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTournamentStreams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/GetTournamentStreams', services_dot_stream__service__pb2.GetTournamentStreamsRequest.SerializeToString, services_dot_stream__service__pb2.GetTournamentStreamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetStreamQueue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/GetStreamQueue', services_dot_stream__service__pb2.GetStreamQueueRequest.SerializeToString, services_dot_stream__service__pb2.GetStreamQueueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AddMatchToStreamQueue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/AddMatchToStreamQueue', services_dot_stream__service__pb2.AddMatchToStreamQueueRequest.SerializeToString, services_dot_stream__service__pb2.AddMatchToStreamQueueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RemoveMatchFromStreamQueue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/RemoveMatchFromStreamQueue', services_dot_stream__service__pb2.RemoveMatchFromStreamQueueRequest.SerializeToString, services_dot_stream__service__pb2.RemoveMatchFromStreamQueueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ReorderStreamQueueEntry(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parrygg.services.StreamService/ReorderStreamQueueEntry', services_dot_stream__service__pb2.ReorderStreamQueueEntryRequest.SerializeToString, services_dot_stream__service__pb2.ReorderStreamQueueEntryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)