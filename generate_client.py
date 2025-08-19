#!/usr/bin/env python3
"""Generate gRPC client code from proto files for development"""

import os
import subprocess
import sys
from pathlib import Path


def main():
    """Generate gRPC client code from proto files"""
    script_dir = Path(__file__).parent
    proto_dir = script_dir / "protos" / "src"
    output_dir = script_dir / "parrygg" / "generated"
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Create __init__.py in generated directory
    (output_dir / "__init__.py").touch()
    
    # Find all proto files
    proto_files = []
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                proto_files.append(os.path.join(root, file))
    
    if not proto_files:
        print("No proto files found in", proto_dir)
        return 1
    
    # Generate Python code
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
        print(f"Successfully generated client code in {output_dir}")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error generating client code: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())