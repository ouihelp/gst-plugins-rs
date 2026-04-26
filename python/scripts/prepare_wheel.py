#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_INPUT = Path("target/aarch64-apple-darwin/release/libgstrswebrtc.dylib")
DEFAULT_OUTPUT_DIR = Path("python/src/gst_plugins_rs/lib/gstreamer-1.0")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    source = args.input.resolve()
    if not source.exists():
        raise SystemExit(f"Missing built plugin: {source}")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / source.name
    shutil.copy2(source, target)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
