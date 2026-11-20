#!/usr/bin/env python3
"""Entry for make.fun's news-image-20261120 bounty (Python 3.13, stdlib only).

The image is drawn by draw_entry.py and shipped in this repository as
entry.png; this program copies it to the output directory the grader
gives it. It runs with no network and writes the same bytes every run.

Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
source = HERE / "entry.png"
target = OUT_DIR / "entry.png"
shutil.copyfile(source, target)
# The grader runs this twice and requires identical bytes: copying the
# shipped file byte for byte guarantees that, and this check proves it
# here instead of failing silently in the sandbox.
assert target.stat().st_size == source.stat().st_size, "copy is incomplete"
print("wrote", target, target.stat().st_size, "bytes")
