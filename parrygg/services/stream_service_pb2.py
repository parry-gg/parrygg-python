"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'services/stream_service.proto')
_sym_db = _symbol_database.Default()
from ..models import stream_pb2 as models_dot_stream__pb2
from ..models import tournament_pb2 as models_dot_tournament__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dservices/stream_service.proto\x12\x10parrygg.services\x1a\x13models/stream.proto\x1a\x17models/tournament.proto"\x8a\x01\n\x13CreateStreamRequest\x12C\n\x15tournament_identifier\x18\x01 \x01(\x0b2$.parrygg.models.TournamentIdentifier\x12.\n\x06stream\x18\x02 \x01(\x0b2\x1e.parrygg.models.StreamMutation">\n\x14CreateStreamResponse\x12&\n\x06stream\x18\x01 \x01(\x0b2\x16.parrygg.models.Stream"Q\n\x13UpdateStreamRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\x06stream\x18\x02 \x01(\x0b2\x1e.parrygg.models.StreamMutation">\n\x14UpdateStreamResponse\x12&\n\x06stream\x18\x01 \x01(\x0b2\x16.parrygg.models.Stream"!\n\x13DeleteStreamRequest\x12\n\n\x02id\x18\x01 \x01(\t"\x16\n\x14DeleteStreamResponse"b\n\x1bGetTournamentStreamsRequest\x12C\n\x15tournament_identifier\x18\x01 \x01(\x0b2$.parrygg.models.TournamentIdentifier"G\n\x1cGetTournamentStreamsResponse\x12\'\n\x07streams\x18\x01 \x03(\x0b2\x16.parrygg.models.Stream"*\n\x15GetStreamQueueRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t"K\n\x16GetStreamQueueResponse\x121\n\x07entries\x18\x01 \x03(\x0b2 .parrygg.models.StreamQueueEntry"C\n\x1cAddMatchToStreamQueueRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x10\n\x08match_id\x18\x02 \x01(\t"P\n\x1dAddMatchToStreamQueueResponse\x12/\n\x05entry\x18\x01 \x01(\x0b2 .parrygg.models.StreamQueueEntry"5\n!RemoveMatchFromStreamQueueRequest\x12\x10\n\x08entry_id\x18\x01 \x01(\t"$\n"RemoveMatchFromStreamQueueResponse"H\n\x1eReorderStreamQueueEntryRequest\x12\x10\n\x08entry_id\x18\x01 \x01(\t\x12\x14\n\x0cnew_position\x18\x02 \x01(\x05"!\n\x1fReorderStreamQueueEntryResponse2\x9d\x07\n\rStreamService\x12_\n\x0cCreateStream\x12%.parrygg.services.CreateStreamRequest\x1a&.parrygg.services.CreateStreamResponse"\x00\x12_\n\x0cUpdateStream\x12%.parrygg.services.UpdateStreamRequest\x1a&.parrygg.services.UpdateStreamResponse"\x00\x12_\n\x0cDeleteStream\x12%.parrygg.services.DeleteStreamRequest\x1a&.parrygg.services.DeleteStreamResponse"\x00\x12w\n\x14GetTournamentStreams\x12-.parrygg.services.GetTournamentStreamsRequest\x1a..parrygg.services.GetTournamentStreamsResponse"\x00\x12e\n\x0eGetStreamQueue\x12\'.parrygg.services.GetStreamQueueRequest\x1a(.parrygg.services.GetStreamQueueResponse"\x00\x12z\n\x15AddMatchToStreamQueue\x12..parrygg.services.AddMatchToStreamQueueRequest\x1a/.parrygg.services.AddMatchToStreamQueueResponse"\x00\x12\x89\x01\n\x1aRemoveMatchFromStreamQueue\x123.parrygg.services.RemoveMatchFromStreamQueueRequest\x1a4.parrygg.services.RemoveMatchFromStreamQueueResponse"\x00\x12\x80\x01\n\x17ReorderStreamQueueEntry\x120.parrygg.services.ReorderStreamQueueEntryRequest\x1a1.parrygg.services.ReorderStreamQueueEntryResponse"\x00B\x1a\n\x16gg.parry.grpc.servicesP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.stream_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16gg.parry.grpc.servicesP\x01'
    _globals['_CREATESTREAMREQUEST']._serialized_start = 98
    _globals['_CREATESTREAMREQUEST']._serialized_end = 236
    _globals['_CREATESTREAMRESPONSE']._serialized_start = 238
    _globals['_CREATESTREAMRESPONSE']._serialized_end = 300
    _globals['_UPDATESTREAMREQUEST']._serialized_start = 302
    _globals['_UPDATESTREAMREQUEST']._serialized_end = 383
    _globals['_UPDATESTREAMRESPONSE']._serialized_start = 385
    _globals['_UPDATESTREAMRESPONSE']._serialized_end = 447
    _globals['_DELETESTREAMREQUEST']._serialized_start = 449
    _globals['_DELETESTREAMREQUEST']._serialized_end = 482
    _globals['_DELETESTREAMRESPONSE']._serialized_start = 484
    _globals['_DELETESTREAMRESPONSE']._serialized_end = 506
    _globals['_GETTOURNAMENTSTREAMSREQUEST']._serialized_start = 508
    _globals['_GETTOURNAMENTSTREAMSREQUEST']._serialized_end = 606
    _globals['_GETTOURNAMENTSTREAMSRESPONSE']._serialized_start = 608
    _globals['_GETTOURNAMENTSTREAMSRESPONSE']._serialized_end = 679
    _globals['_GETSTREAMQUEUEREQUEST']._serialized_start = 681
    _globals['_GETSTREAMQUEUEREQUEST']._serialized_end = 723
    _globals['_GETSTREAMQUEUERESPONSE']._serialized_start = 725
    _globals['_GETSTREAMQUEUERESPONSE']._serialized_end = 800
    _globals['_ADDMATCHTOSTREAMQUEUEREQUEST']._serialized_start = 802
    _globals['_ADDMATCHTOSTREAMQUEUEREQUEST']._serialized_end = 869
    _globals['_ADDMATCHTOSTREAMQUEUERESPONSE']._serialized_start = 871
    _globals['_ADDMATCHTOSTREAMQUEUERESPONSE']._serialized_end = 951
    _globals['_REMOVEMATCHFROMSTREAMQUEUEREQUEST']._serialized_start = 953
    _globals['_REMOVEMATCHFROMSTREAMQUEUEREQUEST']._serialized_end = 1006
    _globals['_REMOVEMATCHFROMSTREAMQUEUERESPONSE']._serialized_start = 1008
    _globals['_REMOVEMATCHFROMSTREAMQUEUERESPONSE']._serialized_end = 1044
    _globals['_REORDERSTREAMQUEUEENTRYREQUEST']._serialized_start = 1046
    _globals['_REORDERSTREAMQUEUEENTRYREQUEST']._serialized_end = 1118
    _globals['_REORDERSTREAMQUEUEENTRYRESPONSE']._serialized_start = 1120
    _globals['_REORDERSTREAMQUEUEENTRYRESPONSE']._serialized_end = 1153
    _globals['_STREAMSERVICE']._serialized_start = 1156
    _globals['_STREAMSERVICE']._serialized_end = 2081