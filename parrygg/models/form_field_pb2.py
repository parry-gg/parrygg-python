"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/form_field.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17models/form_field.proto\x12\x0eparrygg.models\x1a\x1cgoogle/protobuf/struct.proto"\xa1\x01\n\tFormField\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x121\n\nfield_type\x18\x03 \x01(\x0e2\x1d.parrygg.models.FormFieldType\x12\x0f\n\x07options\x18\x04 \x03(\t\x12\x10\n\x08required\x18\x05 \x01(\x08\x12\x12\n\nsort_order\x18\x06 \x01(\x05\x12\x0f\n\x07enabled\x18\x07 \x01(\x08"\xf7\x01\n\x11FormFieldMutation\x12\x12\n\x05label\x18\x01 \x01(\tH\x00\x88\x01\x01\x126\n\nfield_type\x18\x02 \x01(\x0e2\x1d.parrygg.models.FormFieldTypeH\x01\x88\x01\x01\x12\x0f\n\x07options\x18\x03 \x03(\t\x12\x15\n\x08required\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x17\n\nsort_order\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x14\n\x07enabled\x18\x06 \x01(\x08H\x04\x88\x01\x01B\x08\n\x06_labelB\r\n\x0b_field_typeB\x0b\n\t_requiredB\r\n\x0b_sort_orderB\n\n\x08_enabled"W\n\x19FormFieldResponseMutation\x12\x10\n\x08field_id\x18\x01 \x01(\t\x12(\n\x08response\x18\x02 \x01(\x0b2\x16.google.protobuf.Value"\x91\x01\n\x11FormFieldResponse\x12\x10\n\x08field_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x121\n\nfield_type\x18\x03 \x01(\x0e2\x1d.parrygg.models.FormFieldType\x12(\n\x08response\x18\x04 \x01(\x0b2\x16.google.protobuf.Value*\xc9\x01\n\rFormFieldType\x12\x1f\n\x1bFORM_FIELD_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14FORM_FIELD_TYPE_TEXT\x10\x01\x12!\n\x1dFORM_FIELD_TYPE_SINGLE_SELECT\x10\x02\x12 \n\x1cFORM_FIELD_TYPE_MULTI_SELECT\x10\x03\x12\x1b\n\x17FORM_FIELD_TYPE_BOOLEAN\x10\x04\x12\x1b\n\x17FORM_FIELD_TYPE_NUMERIC\x10\x05B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.form_field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_FORMFIELDTYPE']._serialized_start = 725
    _globals['_FORMFIELDTYPE']._serialized_end = 926
    _globals['_FORMFIELD']._serialized_start = 74
    _globals['_FORMFIELD']._serialized_end = 235
    _globals['_FORMFIELDMUTATION']._serialized_start = 238
    _globals['_FORMFIELDMUTATION']._serialized_end = 485
    _globals['_FORMFIELDRESPONSEMUTATION']._serialized_start = 487
    _globals['_FORMFIELDRESPONSEMUTATION']._serialized_end = 574
    _globals['_FORMFIELDRESPONSE']._serialized_start = 577
    _globals['_FORMFIELDRESPONSE']._serialized_end = 722