#!/usr/bin/env python3
"""Generate gRPC client code from proto files for development"""

import os
import re
import subprocess
import sys
from pathlib import Path


def main():
    """Generate gRPC client code from proto files"""
    script_dir = Path(__file__).parent
    proto_dir = script_dir / "protos" / "src"
    output_dir = script_dir / "parrygg"
    
    # Find all proto files
    proto_files = []
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                proto_files.append(os.path.join(root, file))
    
    if not proto_files:
        print("No proto files found in", proto_dir)
        return 1
    
    # Generate Python code directly to parrygg directory
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir}",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
    ]
    cmd.extend(proto_files)
    
    print("Generating gRPC client code...")
    print(" ".join(cmd))
    
    try:
        subprocess.run(cmd, check=True)
        
        # Create __init__.py files where needed
        services_dir = output_dir / "services"
        models_dir = output_dir / "models"
        
        if services_dir.exists():
            (services_dir / "__init__.py").write_text('"""gRPC services for parry.gg API"""\n')
        
        if models_dir.exists():
            (models_dir / "__init__.py").write_text('"""Protocol buffer models for parry.gg API"""\n')
        
        print(f"Successfully generated client code in {output_dir}")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error generating client code: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
