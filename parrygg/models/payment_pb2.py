"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/payment.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14models/payment.proto\x12\x0eparrygg.models\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto*\xac\x01\n\x12TournamentPassType\x12$\n TOURNAMENT_PASS_TYPE_UNSPECIFIED\x10\x00\x12"\n\x1eTOURNAMENT_PASS_TYPE_SPECTATOR\x10\x01\x12#\n\x1fTOURNAMENT_PASS_TYPE_COMPETITOR\x10\x02\x12\'\n#TOURNAMENT_PASS_TYPE_VENUE_FEE_ONLY\x10\x03B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.payment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_TOURNAMENTPASSTYPE']._serialized_start = 104
    _globals['_TOURNAMENTPASSTYPE']._serialized_end = 276