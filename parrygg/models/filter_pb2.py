"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'models/filter.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..models import bracket_pb2 as models_dot_bracket__pb2
from ..models import event_pb2 as models_dot_event__pb2
from ..models import phase_pb2 as models_dot_phase__pb2
from ..models import tournament_pb2 as models_dot_tournament__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13models/filter.proto\x12\x0eparrygg.models\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14models/bracket.proto\x1a\x12models/event.proto\x1a\x12models/phase.proto\x1a\x17models/tournament.proto"0\n\x0cEventsFilter\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01B\n\n\x08_user_id"\xbe\x02\n\x11TournamentsFilter\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x126\n\x0cadmin_filter\x18\x03 \x01(\x0b2\x1b.parrygg.models.AdminFilterH\x02\x88\x01\x01\x12\x11\n\x04name\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0bcustom_slug\x18\x05 \x01(\tH\x04\x88\x01\x01\x12<\n\x13event_updated_since\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x05\x88\x01\x01B\n\n\x08_user_idB\x0b\n\t_owner_idB\x0f\n\r_admin_filterB\x07\n\x05_nameB\x0e\n\x0c_custom_slugB\x16\n\x14_event_updated_since"\x99\x01\n\x0bUsersFilter\x12\x16\n\tgamer_tag\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08event_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12$\n\x17include_anonymous_users\x18\x03 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_gamer_tagB\x0b\n\t_event_idB\x1a\n\x18_include_anonymous_users"Y\n\x0bAdminFilter\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x129\n\npermission\x18\x02 \x01(\x0e2%.parrygg.models.AdminFilterPermission"\xdf\x03\n\rMatchesFilter\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nentrant_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12.\n\x05state\x18\x03 \x01(\x0e2\x1a.parrygg.models.MatchStateH\x02\x88\x01\x01\x129\n\x10tournament_state\x18\x04 \x03(\x0e2\x1f.parrygg.models.TournamentState\x127\n\x07bracket\x18\x05 \x01(\x0b2!.parrygg.models.BracketIdentifierH\x03\x88\x01\x01\x123\n\x05phase\x18\x06 \x01(\x0b2\x1f.parrygg.models.PhaseIdentifierH\x04\x88\x01\x01\x123\n\x05event\x18\x07 \x01(\x0b2\x1f.parrygg.models.EventIdentifierH\x05\x88\x01\x01\x12=\n\ntournament\x18\x08 \x01(\x0b2$.parrygg.models.TournamentIdentifierH\x06\x88\x01\x01B\n\n\x08_user_idB\r\n\x0b_entrant_idB\x08\n\x06_stateB\n\n\x08_bracketB\x08\n\x06_phaseB\x08\n\x06_eventB\r\n\x0b_tournament*_\n\x14TournamentsSortOrder\x12&\n"TOURNAMENTS_SORT_ORDER_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTOURNAMENTS_SORT_ORDER_HOME\x10\x01*\xa6\x01\n\x15AdminFilterPermission\x12\x1f\n\x1bADMIN_FILTER_PERMISSION_ANY\x10\x00\x12!\n\x1dADMIN_FILTER_PERMISSION_ADMIN\x10\x01\x12#\n\x1fADMIN_FILTER_PERMISSION_MANAGER\x10\x02\x12$\n ADMIN_FILTER_PERMISSION_REPORTER\x10\x03B\x18\n\x14gg.parry.grpc.modelsP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14gg.parry.grpc.modelsP\x01'
    _globals['_TOURNAMENTSSORTORDER']._serialized_start = 1259
    _globals['_TOURNAMENTSSORTORDER']._serialized_end = 1354
    _globals['_ADMINFILTERPERMISSION']._serialized_start = 1357
    _globals['_ADMINFILTERPERMISSION']._serialized_end = 1523
    _globals['_EVENTSFILTER']._serialized_start = 159
    _globals['_EVENTSFILTER']._serialized_end = 207
    _globals['_TOURNAMENTSFILTER']._serialized_start = 210
    _globals['_TOURNAMENTSFILTER']._serialized_end = 528
    _globals['_USERSFILTER']._serialized_start = 531
    _globals['_USERSFILTER']._serialized_end = 684
    _globals['_ADMINFILTER']._serialized_start = 686
    _globals['_ADMINFILTER']._serialized_end = 775
    _globals['_MATCHESFILTER']._serialized_start = 778
    _globals['_MATCHESFILTER']._serialized_end = 1257