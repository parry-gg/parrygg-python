"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'services/tournament_service.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..models import form_field_pb2 as models_dot_form__field__pb2
from ..models import tournament_pb2 as models_dot_tournament__pb2
from ..models import image_pb2 as models_dot_image__pb2
from ..models import filter_pb2 as models_dot_filter__pb2
from ..models import pagination_pb2 as models_dot_pagination__pb2
from ..models import payment_pb2 as models_dot_payment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!services/tournament_service.proto\x12\x10parrygg.services\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17models/form_field.proto\x1a\x17models/tournament.proto\x1a\x12models/image.proto\x1a\x13models/filter.proto\x1a\x17models/pagination.proto\x1a\x14models/payment.proto"\x92\x01\n\x14GetTournamentRequest\x12\x0c\n\x02id\x18\x01 \x01(\tH\x00\x12\x19\n\x0ftournament_slug\x18\x02 \x01(\tH\x00\x12C\n\x15tournament_identifier\x18\x03 \x01(\x0b2$.parrygg.models.TournamentIdentifierB\x0c\n\nidentifier"G\n\x15GetTournamentResponse\x12.\n\ntournament\x18\x01 \x01(\x0b2\x1a.parrygg.models.Tournament"\xa2\x01\n\x17UpdateTournamentRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12C\n\x15tournament_identifier\x18\x03 \x01(\x0b2$.parrygg.models.TournamentIdentifier\x126\n\ntournament\x18\x02 \x01(\x0b2".parrygg.models.TournamentMutation"J\n\x18UpdateTournamentResponse\x12.\n\nTournament\x18\x01 \x01(\x0b2\x1a.parrygg.models.Tournament"3\n\x15GetTournamentsOptions\x12\x1a\n\x12return_permissions\x18\x01 \x01(\x08"\xfd\x01\n\x15GetTournamentsRequest\x121\n\x06filter\x18\x01 \x01(\x0b2!.parrygg.models.TournamentsFilter\x128\n\x07options\x18\x02 \x01(\x0b2\'.parrygg.services.GetTournamentsOptions\x12=\n\x12pagination_request\x18\x03 \x01(\x0b2!.parrygg.models.PaginationRequest\x128\n\nsort_order\x18\x04 \x01(\x0e2$.parrygg.models.TournamentsSortOrder"\xdc\x02\n\x16GetTournamentsResponse\x12/\n\x0btournaments\x18\x01 \x03(\x0b2\x1a.parrygg.models.Tournament\x12c\n\x16tournament_permissions\x18\x02 \x03(\x0b2C.parrygg.services.GetTournamentsResponse.TournamentPermissionsEntry\x12?\n\x13pagination_response\x18\x03 \x01(\x0b2".parrygg.models.PaginationResponse\x1ak\n\x1aTournamentPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.parrygg.models.TournamentPermissionsMetadata:\x028\x01"{\n\x1dGetTournamentAttendeesRequest\x12\x15\n\rtournament_id\x18\x01 \x01(\t\x12C\n\x15tournament_identifier\x18\x02 \x01(\x0b2$.parrygg.models.TournamentIdentifier"W\n\x1eGetTournamentAttendeesResponse\x125\n\tattendees\x18\x01 \x03(\x0b2".parrygg.models.TournamentAttendee"\xb3\x01\n\x1aGetTournamentAdminsRequest\x12\x15\n\rtournament_id\x18\x01 \x01(\t\x12C\n\x15tournament_identifier\x18\x03 \x01(\x0b2$.parrygg.models.TournamentIdentifier\x129\n\npermission\x18\x02 \x01(\x0e2%.parrygg.models.AdminFilterPermission"N\n\x1bGetTournamentAdminsResponse\x12/\n\x06admins\x18\x01 \x03(\x0b2\x1f.parrygg.models.TournamentAdmin2\xc0\x04\n\x11TournamentService\x12b\n\rGetTournament\x12&.parrygg.services.GetTournamentRequest\x1a\'.parrygg.services.GetTournamentResponse"\x00\x12e\n\x0eGetTournaments\x12\'.parrygg.services.GetTournamentsRequest\x1a(.parrygg.services.GetTournamentsResponse"\x00\x12}\n\x16GetTournamentAttendees\x12/.parrygg.services.GetTournamentAttendeesRequest\x1a0.parrygg.services.GetTournamentAttendeesResponse"\x00\x12k\n\x10UpdateTournament\x12).parrygg.services.UpdateTournamentRequest\x1a*.parrygg.services.UpdateTournamentResponse"\x00\x12t\n\x13GetTournamentAdmins\x12,.parrygg.services.GetTournamentAdminsRequest\x1a-.parrygg.services.GetTournamentAdminsResponse"\x00B\x1a\n\x16gg.parry.grpc.servicesP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.tournament_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16gg.parry.grpc.servicesP\x01'
    _globals['_GETTOURNAMENTSRESPONSE_TOURNAMENTPERMISSIONSENTRY']._loaded_options = None
    _globals['_GETTOURNAMENTSRESPONSE_TOURNAMENTPERMISSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_GETTOURNAMENTREQUEST']._serialized_start = 227
    _globals['_GETTOURNAMENTREQUEST']._serialized_end = 373
    _globals['_GETTOURNAMENTRESPONSE']._serialized_start = 375
    _globals['_GETTOURNAMENTRESPONSE']._serialized_end = 446
    _globals['_UPDATETOURNAMENTREQUEST']._serialized_start = 449
    _globals['_UPDATETOURNAMENTREQUEST']._serialized_end = 611
    _globals['_UPDATETOURNAMENTRESPONSE']._serialized_start = 613
    _globals['_UPDATETOURNAMENTRESPONSE']._serialized_end = 687
    _globals['_GETTOURNAMENTSOPTIONS']._serialized_start = 689
    _globals['_GETTOURNAMENTSOPTIONS']._serialized_end = 740
    _globals['_GETTOURNAMENTSREQUEST']._serialized_start = 743
    _globals['_GETTOURNAMENTSREQUEST']._serialized_end = 996
    _globals['_GETTOURNAMENTSRESPONSE']._serialized_start = 999
    _globals['_GETTOURNAMENTSRESPONSE']._serialized_end = 1347
    _globals['_GETTOURNAMENTSRESPONSE_TOURNAMENTPERMISSIONSENTRY']._serialized_start = 1240
    _globals['_GETTOURNAMENTSRESPONSE_TOURNAMENTPERMISSIONSENTRY']._serialized_end = 1347
    _globals['_GETTOURNAMENTATTENDEESREQUEST']._serialized_start = 1349
    _globals['_GETTOURNAMENTATTENDEESREQUEST']._serialized_end = 1472
    _globals['_GETTOURNAMENTATTENDEESRESPONSE']._serialized_start = 1474
    _globals['_GETTOURNAMENTATTENDEESRESPONSE']._serialized_end = 1561
    _globals['_GETTOURNAMENTADMINSREQUEST']._serialized_start = 1564
    _globals['_GETTOURNAMENTADMINSREQUEST']._serialized_end = 1743
    _globals['_GETTOURNAMENTADMINSRESPONSE']._serialized_start = 1745
    _globals['_GETTOURNAMENTADMINSRESPONSE']._serialized_end = 1823
    _globals['_TOURNAMENTSERVICE']._serialized_start = 1826
    _globals['_TOURNAMENTSERVICE']._serialized_end = 2402