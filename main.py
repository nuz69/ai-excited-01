"""
Deterministic entry generator for make.fun ai-excited-01 competition.

This program reads 'excited.jpg' relative to main.py's directory and copies
its exact bytes to $MAKEFUN_OUTPUT_DIR/entry.png (defaulting to /output/entry.png).
The output directory is created if it does not exist.
"""

import os
import sys

MAX_BYTES = 1048576  # 1 MiB limit


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "excited.jpg")

    if not os.path.exists(source_path):
        sys.exit(f"Error: Source image not found at {source_path}")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.png")

    with open(source_path, "rb") as f_in:
        data = f_in.read()

    byte_count = len(data)
    if byte_count > MAX_BYTES:
        sys.exit(f"Error: Image size ({byte_count} bytes) exceeds maximum limit of {MAX_BYTES} bytes (1 MiB).")

    with open(output_path, "wb") as f_out:
        f_out.write(data)

    # Post-copy verification: re-read output and confirm byte identity
    with open(output_path, "rb") as f_verify:
        written_data = f_verify.read()

    if written_data != data:
        sys.exit("Error: Output file content does not match source file content.")

    print(f"Output path: {output_path}")
    print(f"Byte count: {byte_count}")
    print("Verification successful: Source and output bytes are identical.")


if __name__ == "__main__":
    main()
