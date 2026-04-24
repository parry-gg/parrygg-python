"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'models/wave.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11models/wave.proto\x12\x0eparrygg.models\x1a\x1fgoogle/protobuf/timestamp.proto"z\n\x04Wave\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08start_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12*\n\x06end_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa6\x01\n\x0cWaveMutation\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x121\n\x08start_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12/\n\x06end_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x02\x88\x01\x01B\x07\n\x05_nameB\x0b\n\t_start_atB\t\n\x07_end_atB\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.wave_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_WAVE']._serialized_start = 70
    _globals['_WAVE']._serialized_end = 192
    _globals['_WAVEMUTATION']._serialized_start = 195
    _globals['_WAVEMUTATION']._serialized_end = 361