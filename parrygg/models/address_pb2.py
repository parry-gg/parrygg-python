"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/address.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14models/address.proto\x12\x0eparrygg.models\x1a\x1fgoogle/protobuf/timestamp.proto"\xe7\x03\n\x07Address\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x19\n\x11formatted_address\x18\x04 \x01(\t\x12\x0f\n\x07country\x18\x05 \x01(\t\x12\x14\n\x0ccountry_code\x18\x06 \x01(\t\x12#\n\x1badministrative_area_level_1\x18\x07 \x01(\t\x12#\n\x1badministrative_area_level_2\x18\x08 \x01(\t\x12\x10\n\x08locality\x18\t \x01(\t\x12\x13\n\x0bsublocality\x18\n \x01(\t\x12\x13\n\x0bpostal_code\x18\x0b \x01(\t\x12\x15\n\rstreet_number\x18\x0c \x01(\t\x12\r\n\x05route\x18\r \x01(\t\x12\x0f\n\x07premise\x18\x0e \x01(\t\x12\x10\n\x08place_id\x18\x0f \x01(\t\x12:\n\rlocation_type\x18\x10 \x01(\x0e2#.parrygg.models.AddressLocationType\x12.\n\ncreated_at\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x12 \x01(\x0b2\x1a.google.protobuf.Timestamp*\xe0\x01\n\x13AddressLocationType\x12%\n!ADDRESS_LOCATION_TYPE_UNSPECIFIED\x10\x00\x12!\n\x1dADDRESS_LOCATION_TYPE_ROOFTOP\x10\x01\x12,\n(ADDRESS_LOCATION_TYPE_RANGE_INTERPOLATED\x10\x02\x12*\n&ADDRESS_LOCATION_TYPE_GEOMETRIC_CENTER\x10\x03\x12%\n!ADDRESS_LOCATION_TYPE_APPROXIMATE\x10\x04B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.address_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_ADDRESSLOCATIONTYPE']._serialized_start = 564
    _globals['_ADDRESSLOCATIONTYPE']._serialized_end = 788
    _globals['_ADDRESS']._serialized_start = 74
    _globals['_ADDRESS']._serialized_end = 561