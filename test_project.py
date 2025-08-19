#!/usr/bin/env python3
"""
Simple test project to demonstrate usage of the parrygg Python package.
"""

import grpc
from parrygg.services.tournament_service_pb2_grpc import TournamentServiceStub
from parrygg.services.tournament_service_pb2 import GetTournamentsRequest


def main():
    # Create a secure gRPC channel to parry.gg API
    channel = grpc.secure_channel("api.parry.gg:443", grpc.ssl_channel_credentials())
    
    # Create a tournament service stub
    tournament_service = TournamentServiceStub(channel)
    
    try:
        # Create a request to get tournaments
        request = GetTournamentsRequest()
        
        # Make the API call
        response = tournament_service.GetTournaments(request)
        
        print("Successfully connected to parry.gg API!")
        print(f"Response: {response}")
        
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        channel.close()


if __name__ == "__main__":
    main()
