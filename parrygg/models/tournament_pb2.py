"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/tournament.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..models import address_pb2 as models_dot_address__pb2
from ..models import image_pb2 as models_dot_image__pb2
from ..models import event_pb2 as models_dot_event__pb2
from ..models import group_pb2 as models_dot_group__pb2
from ..models import form_field_pb2 as models_dot_form__field__pb2
from ..models import payment_pb2 as models_dot_payment__pb2
from ..models import slug_pb2 as models_dot_slug__pb2
from ..models import user_pb2 as models_dot_user__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17models/tournament.proto\x12\x0eparrygg.models\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14models/address.proto\x1a\x12models/image.proto\x1a\x12models/event.proto\x1a\x12models/group.proto\x1a\x17models/form_field.proto\x1a\x14models/payment.proto\x1a\x11models/slug.proto\x1a\x11models/user.proto"\xcf\x08\n\nTournament\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x15\n\rvenue_address\x18\x04 \x01(\t\x12\x15\n\radmin_contact\x18\x07 \x01(\t\x12\x15\n\rcurrency_code\x18\x08 \x01(\t\x12.\n\nstart_date\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_date\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\x05state\x18\x0b \x01(\x0e2\x1f.parrygg.models.TournamentState\x12%\n\x06images\x18\x0c \x03(\x0b2\x15.parrygg.models.Image\x12%\n\x06events\x18\r \x03(\x0b2\x15.parrygg.models.Event\x12\x15\n\rnum_attendees\x18\x0e \x01(\x05\x12\x10\n\x08owner_id\x18\x0f \x01(\t\x12#\n\x05slugs\x18\x10 \x03(\x0b2\x14.parrygg.models.Slug\x12\x11\n\tvenue_fee\x18\x11 \x01(\x05\x12\x11\n\ttime_zone\x18\x12 \x01(\t\x129\n\x10visibility_level\x18\x13 \x01(\x0e2\x1f.parrygg.models.VisibilityLevel\x12-\n\x07address\x18\x14 \x01(\x0b2\x17.parrygg.models.AddressH\x00\x88\x01\x01\x123\n\rlocation_type\x18\x15 \x01(\x0e2\x1c.parrygg.models.LocationType\x12;\n\x17registration_start_date\x18\x16 \x01(\x0b2\x1a.google.protobuf.Timestamp\x129\n\x15registration_end_date\x18\x17 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\ncreated_at\x18\x18 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x19 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x0eentry_fee_type\x18\x1a \x01(\x0e2\x1c.parrygg.models.EntryFeeType\x12;\n\x0crequirements\x18\x1b \x03(\x0b2%.parrygg.models.TournamentRequirement\x126\n\x10ui_customization\x18\x1c \x01(\x0b2\x17.google.protobuf.StructH\x01\x88\x01\x01\x12;\n\x18registration_form_fields\x18\x1d \x03(\x0b2\x19.parrygg.models.FormFieldB\n\n\x08_addressB\x13\n\x11_ui_customization"\xfd\x06\n\x12TournamentMutation\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nshort_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rvenue_address\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\radmin_contact\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\x07 \x01(\tH\x04\x88\x01\x01\x123\n\nstart_date\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x05\x88\x01\x01\x121\n\x08end_date\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampH\x06\x88\x01\x01\x12\x15\n\x08owner_id\x18\n \x01(\tH\x07\x88\x01\x01\x12\x16\n\tvenue_fee\x18\x0b \x01(\x05H\x08\x88\x01\x01\x12\x16\n\ttime_zone\x18\x0c \x01(\tH\t\x88\x01\x01\x12>\n\x10visibility_level\x18\r \x01(\x0e2\x1f.parrygg.models.VisibilityLevelH\n\x88\x01\x01\x128\n\rlocation_type\x18\x0e \x01(\x0e2\x1c.parrygg.models.LocationTypeH\x0b\x88\x01\x01\x12@\n\x17registration_start_date\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampH\x0c\x88\x01\x01\x12>\n\x15registration_end_date\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampH\r\x88\x01\x01\x129\n\x0eentry_fee_type\x18\x11 \x01(\x0e2\x1c.parrygg.models.EntryFeeTypeH\x0e\x88\x01\x01B\x07\n\x05_nameB\r\n\x0b_short_nameB\x10\n\x0e_venue_addressB\x10\n\x0e_admin_contactB\x10\n\x0e_currency_codeB\r\n\x0b_start_dateB\x0b\n\t_end_dateB\x0b\n\t_owner_idB\x0c\n\n_venue_feeB\x0c\n\n_time_zoneB\x13\n\x11_visibility_levelB\x10\n\x0e_location_typeB\x1a\n\x18_registration_start_dateB\x18\n\x16_registration_end_dateB\x11\n\x0f_entry_fee_type"K\n\x0bPageContent\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x12\n\ncontent_md\x18\x04 \x01(\t"x\n\x12MutablePageContent\x12\x12\n\x05index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ncontent_md\x18\x03 \x01(\tH\x02\x88\x01\x01B\x08\n\x06_indexB\x08\n\x06_titleB\r\n\x0b_content_md"\xa3\x02\n\x16TournamentRegistration\x12\x15\n\rtournament_id\x18\x01 \x01(\t\x12\x16\n\x0epaid_venue_fee\x18\x03 \x01(\x08\x12>\n\x13event_registrations\x18\x04 \x03(\x0b2!.parrygg.models.EventRegistration\x12"\n\x04user\x18\x05 \x01(\x0b2\x14.parrygg.models.User\x125\n\tpass_type\x18\x06 \x01(\x0e2".parrygg.models.TournamentPassType\x129\n\x0eform_responses\x18\x08 \x03(\x0b2!.parrygg.models.FormFieldResponseJ\x04\x08\x02\x10\x03"\x9e\x01\n\x1eTournamentRegistrationMutation\x12\x1b\n\x0epaid_venue_fee\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12F\n\x13event_registrations\x18\x02 \x03(\x0b2).parrygg.models.EventRegistrationMutationB\x11\n\x0f_paid_venue_feeJ\x04\x08\x03\x10\x04"|\n#BatchTournamentRegistrationMutation\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12D\n\x0cregistration\x18\x02 \x01(\x0b2..parrygg.models.TournamentRegistrationMutation"i\n\x12TournamentAttendee\x12"\n\x04user\x18\x01 \x01(\x0b2\x14.parrygg.models.User\x12/\n\x06events\x18\x02 \x03(\x0b2\x1f.parrygg.models.EventAttendance"\xa3\x01\n\x0fTournamentAdmin\x12$\n\x04user\x18\x01 \x01(\x0b2\x14.parrygg.models.UserH\x00\x12&\n\x05group\x18\x02 \x01(\x0b2\x15.parrygg.models.GroupH\x00\x128\n\npermission\x18\x03 \x01(\x0e2$.parrygg.models.TournamentPermissionB\x08\n\x06member"M\n\x14TournamentIdentifier\x12\x0c\n\x02id\x18\x01 \x01(\tH\x00\x12\x19\n\x0ftournament_slug\x18\x02 \x01(\tH\x00B\x0c\n\nidentifier"d\n\x1dTournamentPermissionsMetadata\x12C\n\x15tournament_permission\x18\x01 \x01(\x0e2$.parrygg.models.TournamentPermission"Q\n\x12DiscordRequirement\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x13\n\x0binvite_link\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t"1\n\x1cEventRegistrationRequirement\x12\x11\n\tevent_ids\x18\x01 \x03(\t"\xd9\x01\n\x15TournamentRequirement\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12A\n\x13discord_requirement\x18\x03 \x01(\x0b2".parrygg.models.DiscordRequirementH\x00\x12V\n\x1eevent_registration_requirement\x18\x04 \x01(\x0b2,.parrygg.models.EventRegistrationRequirementH\x00B\x0b\n\ttype_data"\xc7\x01\n\x1dTournamentRequirementMutation\x12A\n\x13discord_requirement\x18\x01 \x01(\x0b2".parrygg.models.DiscordRequirementH\x00\x12V\n\x1eevent_registration_requirement\x18\x02 \x01(\x0b2,.parrygg.models.EventRegistrationRequirementH\x00B\x0b\n\ttype_data*\xaf\x01\n\x0fTournamentState\x12 \n\x1cTOURNAMENT_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18TOURNAMENT_STATE_PENDING\x10\x01\x12\x1a\n\x16TOURNAMENT_STATE_READY\x10\x02\x12 \n\x1cTOURNAMENT_STATE_IN_PROGRESS\x10\x03\x12\x1e\n\x1aTOURNAMENT_STATE_COMPLETED\x10\x04*\x91\x01\n\x14TournamentPermission\x12 \n\x1cPERMISSION_LEVEL_UNSPECIFIED\x10\x00\x12\x1a\n\x16PERMISSION_LEVEL_ADMIN\x10\x01\x12\x1c\n\x18PERMISSION_LEVEL_MANAGER\x10\x02\x12\x1d\n\x19PERMISSION_LEVEL_REPORTER\x10\x03*\x8d\x01\n\x0fVisibilityLevel\x12 \n\x1cVISIBILITY_LEVEL_UNSPECIFIED\x10\x00\x12\x1b\n\x17VISIBILITY_LEVEL_PUBLIC\x10\x01\x12\x1e\n\x1aVISIBILITY_LEVEL_LINK_ONLY\x10\x02\x12\x1b\n\x17VISIBILITY_LEVEL_HIDDEN\x10\x03*`\n\x0cEntryFeeType\x12\x1e\n\x1aENTRY_FEE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13ENTRY_FEE_TYPE_FREE\x10\x01\x12\x17\n\x13ENTRY_FEE_TYPE_PAID\x10\x02*\xd7\x01\n\x1eDiscordRequirementFailureCause\x12)\n%REQUIREMENT_FAILURE_CAUSE_UNSPECIFIED\x10\x00\x12-\n)REQUIREMENT_FAILURE_CAUSE_UNAUTHENTICATED\x10\x01\x12.\n*REQUIREMENT_FAILURE_CAUSE_ACCOUNT_UNLINKED\x10\x02\x12+\n\'REQUIREMENT_FAILURE_CAUSE_NOT_IN_SERVER\x10\x03*\xa5\x01\n\x19TournamentRequirementType\x12+\n\'TOURNAMENT_REQUIREMENT_TYPE_UNSPECIFIED\x10\x00\x12\'\n#TOURNAMENT_REQUIREMENT_TYPE_DISCORD\x10\x01\x122\n.TOURNAMENT_REQUIREMENT_TYPE_EVENT_REGISTRATION\x10\x02B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.tournament_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_TOURNAMENTSTATE']._serialized_start = 4066
    _globals['_TOURNAMENTSTATE']._serialized_end = 4241
    _globals['_TOURNAMENTPERMISSION']._serialized_start = 4244
    _globals['_TOURNAMENTPERMISSION']._serialized_end = 4389
    _globals['_VISIBILITYLEVEL']._serialized_start = 4392
    _globals['_VISIBILITYLEVEL']._serialized_end = 4533
    _globals['_ENTRYFEETYPE']._serialized_start = 4535
    _globals['_ENTRYFEETYPE']._serialized_end = 4631
    _globals['_DISCORDREQUIREMENTFAILURECAUSE']._serialized_start = 4634
    _globals['_DISCORDREQUIREMENTFAILURECAUSE']._serialized_end = 4849
    _globals['_TOURNAMENTREQUIREMENTTYPE']._serialized_start = 4852
    _globals['_TOURNAMENTREQUIREMENTTYPE']._serialized_end = 5017
    _globals['_TOURNAMENT']._serialized_start = 274
    _globals['_TOURNAMENT']._serialized_end = 1377
    _globals['_TOURNAMENTMUTATION']._serialized_start = 1380
    _globals['_TOURNAMENTMUTATION']._serialized_end = 2273
    _globals['_PAGECONTENT']._serialized_start = 2275
    _globals['_PAGECONTENT']._serialized_end = 2350
    _globals['_MUTABLEPAGECONTENT']._serialized_start = 2352
    _globals['_MUTABLEPAGECONTENT']._serialized_end = 2472
    _globals['_TOURNAMENTREGISTRATION']._serialized_start = 2475
    _globals['_TOURNAMENTREGISTRATION']._serialized_end = 2766
    _globals['_TOURNAMENTREGISTRATIONMUTATION']._serialized_start = 2769
    _globals['_TOURNAMENTREGISTRATIONMUTATION']._serialized_end = 2927
    _globals['_BATCHTOURNAMENTREGISTRATIONMUTATION']._serialized_start = 2929
    _globals['_BATCHTOURNAMENTREGISTRATIONMUTATION']._serialized_end = 3053
    _globals['_TOURNAMENTATTENDEE']._serialized_start = 3055
    _globals['_TOURNAMENTATTENDEE']._serialized_end = 3160
    _globals['_TOURNAMENTADMIN']._serialized_start = 3163
    _globals['_TOURNAMENTADMIN']._serialized_end = 3326
    _globals['_TOURNAMENTIDENTIFIER']._serialized_start = 3328
    _globals['_TOURNAMENTIDENTIFIER']._serialized_end = 3405
    _globals['_TOURNAMENTPERMISSIONSMETADATA']._serialized_start = 3407
    _globals['_TOURNAMENTPERMISSIONSMETADATA']._serialized_end = 3507
    _globals['_DISCORDREQUIREMENT']._serialized_start = 3509
    _globals['_DISCORDREQUIREMENT']._serialized_end = 3590
    _globals['_EVENTREGISTRATIONREQUIREMENT']._serialized_start = 3592
    _globals['_EVENTREGISTRATIONREQUIREMENT']._serialized_end = 3641
    _globals['_TOURNAMENTREQUIREMENT']._serialized_start = 3644
    _globals['_TOURNAMENTREQUIREMENT']._serialized_end = 3861
    _globals['_TOURNAMENTREQUIREMENTMUTATION']._serialized_start = 3864
    _globals['_TOURNAMENTREQUIREMENTMUTATION']._serialized_end = 4063