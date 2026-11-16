#!/usr/bin/env python3
"""
main.py — Deterministic entry builder for make.fun ai-excited-01.

Resolves excited.jpg relative to this script's directory, ensures the output
directory exists, copies the image bytes to /output/entry.png (or 
MAKEFUN_OUTPUT_DIR/entry.png if specified), verifies byte-for-byte identity
between source and output, and validates size constraints (<= 1 MiB).
Uses Python 3.13 standard library only.
"""

import os
import sys

MAX_SIZE = 1024 * 1024  # 1 MiB

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "excited.jpg")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    target_path = os.path.join(output_dir, "entry.png")
    
    # Read source bytes
    with open(source_path, "rb") as f:
        source_data = f.read()
        
    source_size = len(source_data)
    if source_size > MAX_SIZE:
        print(f"Error: Source image size {source_size} bytes exceeds 1 MiB limit.", file=sys.stderr)
        sys.exit(1)
        
    # Write output bytes
    with open(target_path, "wb") as f:
        f.write(source_data)
        
    # Re-read output bytes to verify
    with open(target_path, "rb") as f:
        target_data = f.read()
        
    if source_data != target_data:
        print("Error: Verification failed — source and output bytes do not match!", file=sys.stderr)
        sys.exit(1)
        
    print("Verification passed: Output bytes match source bytes exactly.")
    print(f"Output path: {target_path}")
    print(f"Byte count: {len(target_data)}")

if __name__ == "__main__":
    main()
