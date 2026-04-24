"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/stream.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13models/stream.proto\x12\x0eparrygg.models"\xac\x01\n\x06Stream\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rtournament_id\x18\x02 \x01(\t\x120\n\x08platform\x18\x03 \x01(\x0e2\x1e.parrygg.models.StreamPlatform\x12\x0f\n\x07channel\x18\x04 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08capacity\x18\x06 \x01(\x05B\x0f\n\r_display_name"\xc6\x01\n\x0eStreamMutation\x125\n\x08platform\x18\x01 \x01(\x0e2\x1e.parrygg.models.StreamPlatformH\x00\x88\x01\x01\x12\x14\n\x07channel\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08capacity\x18\x04 \x01(\x05H\x03\x88\x01\x01B\x0b\n\t_platformB\n\n\x08_channelB\x0f\n\r_display_nameB\x0b\n\t_capacity"\x8d\x01\n\x10StreamQueueEntry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12\x10\n\x08match_id\x18\x03 \x01(\t\x12\x10\n\x08position\x18\x04 \x01(\x05\x126\n\x06status\x18\x05 \x01(\x0e2&.parrygg.models.StreamQueueEntryStatus*j\n\x0eStreamPlatform\x12\x1f\n\x1bSTREAM_PLATFORM_UNSPECIFIED\x10\x00\x12\x1a\n\x16STREAM_PLATFORM_TWITCH\x10\x01\x12\x1b\n\x17STREAM_PLATFORM_YOUTUBE\x10\x02*\x91\x01\n\x16StreamQueueEntryStatus\x12)\n%STREAM_QUEUE_ENTRY_STATUS_UNSPECIFIED\x10\x00\x12$\n STREAM_QUEUE_ENTRY_STATUS_QUEUED\x10\x01\x12&\n"STREAM_QUEUE_ENTRY_STATUS_ONSTREAM\x10\x02B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_STREAMPLATFORM']._serialized_start = 559
    _globals['_STREAMPLATFORM']._serialized_end = 665
    _globals['_STREAMQUEUEENTRYSTATUS']._serialized_start = 668
    _globals['_STREAMQUEUEENTRYSTATUS']._serialized_end = 813
    _globals['_STREAM']._serialized_start = 40
    _globals['_STREAM']._serialized_end = 212
    _globals['_STREAMMUTATION']._serialized_start = 215
    _globals['_STREAMMUTATION']._serialized_end = 413
    _globals['_STREAMQUEUEENTRY']._serialized_start = 416
    _globals['_STREAMQUEUEENTRY']._serialized_end = 557