#!/usr/bin/env python3
"""Convert Jupyter notebooks to marimo format."""

import subprocess
import sys
import shutil
from pathlib import Path


def _is_local_file(path: Path) -> bool:
    try:
        p = path.resolve(strict=True)
    except Exception:
        return False
    return p.is_file()


def convert_jupyter_to_marimo(input_path: str, output_path: str | None = None) -> str:
    """Convert a Jupyter notebook to marimo format.

    Args:
        input_path: Path to .ipynb file (local or GitHub URL)
        output_path: Optional output path. If None, derives from input.

    Returns:
        Path to the created marimo notebook.
    """
    input_file = Path(input_path)

    # Reject remote URLs to avoid executing untrusted network inputs
    if str(input_path).startswith(("http://", "https://")):
        raise ValueError("Remote URLs are not allowed for conversion. Download the file locally first.")

    # Ensure input exists and is a regular local file
    if not _is_local_file(input_file):
        raise FileNotFoundError(f"Input file not found or not a regular file: {input_path}")

    if output_path is None:
        output_path = str(input_file.with_suffix(".py"))

    # Ensure the marimo executable is available
    marimo_exe = shutil.which("marimo")
    if not marimo_exe:
        raise RuntimeError("marimo executable not found in PATH")

    cmd = [marimo_exe, "convert", str(input_file), "-o", str(output_path)]

    try:
        # Use list args (no shell) and a timeout; capture output for diagnostics
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        raise RuntimeError("Conversion timed out")
    except Exception as e:
        raise RuntimeError(f"Conversion failed to start: {e}")

    if result.returncode != 0:
        raise RuntimeError(f"Conversion failed: {result.stderr.strip()}")

    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: convert_notebook.py <input.ipynb> [output.py]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = convert_jupyter_to_marimo(input_file, output_file)
        print(f"Converted to: {result}")
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
