# parrygg-python

Python gRPC client library for the parry.gg tournament platform API.

## Installation

```bash
pip install -e .
```

## Requirements

- Python 3.7+
- grpcio
- grpcio-tools
- protobuf

## Usage

### Basic Example

```python
import grpc
from parrygg.services.tournament_service_pb2_grpc import TournamentServiceStub
from parrygg.services.tournament_service_pb2 import GetTournamentsRequest

# Create a secure gRPC channel
channel = grpc.secure_channel("api.parry.gg:443", grpc.ssl_channel_credentials())

# Create a tournament service stub
tournament_service = TournamentServiceStub(channel)

# Make a request
request = GetTournamentsRequest()
response = tournament_service.GetTournaments(request)

print(f"Found {len(response.tournaments)} tournaments")
channel.close()
```

### Authentication with API Key

For authenticated requests, include your API key in the `X-API-KEY` header:

```python
import grpc
from parrygg.services.tournament_service_pb2_grpc import TournamentServiceStub
from parrygg.services.tournament_service_pb2 import GetTournamentsRequest

# Your API key from developer.parry.gg
API_KEY = "your-api-key-here"

# Create a secure gRPC channel
channel = grpc.secure_channel("api.parry.gg:443", grpc.ssl_channel_credentials())

# Create a tournament service stub
tournament_service = TournamentServiceStub(channel)

# Create metadata with API key
metadata = [("x-api-key", API_KEY)]

# Make an authenticated request
request = GetTournamentsRequest()
response = tournament_service.GetTournaments(request, metadata=metadata)

print(f"Successfully retrieved {len(response.tournaments)} tournaments")
for tournament in response.tournaments:
    print(f"- {tournament.name} (ID: {tournament.id})")

channel.close()
```

## Available Services

The library provides access to all parry.gg API services:

- **TournamentService** - Tournament management and retrieval
- **EventService** - Event operations within tournaments
- **BracketService** - Bracket and match management
- **UserService** - User account operations
- **EntrantService** - Tournament participant management
- **PhaseService** - Tournament phase operations
- **GameService** - Game information and metadata
- **HierarchyService** - Organizational hierarchy management
- **NotificationService** - Notification operations
- **MatchService** - Individual match operations
- **PageContentService** - Content management

## Development

### Regenerating Client Code

To regenerate the client code from proto files:

```bash
python generate_client.py
```

This script:
1. Generates Python code from the proto files using `protoc`
2. Automatically fixes import paths using `protoletariat`
3. Creates necessary `__init__.py` files

### Testing

Run the test script to verify the client works:

```bash
python test_project.py
```

## Documentation

For comprehensive API documentation, authentication details, and developer resources, visit:

**[developer.parry.gg](https://developer.parry.gg)**

The developer portal includes:
- Complete API reference
- Authentication guide
- Code examples
- Rate limiting information
- Webhook documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For API support and questions, please visit [developer.parry.gg](https://developer.parry.gg) or contact the parry.gg development team.