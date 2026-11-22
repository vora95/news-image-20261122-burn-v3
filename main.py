#!/usr/bin/env python3
"""SUNDAY IN FULL, the Sunday 22 November 2026 front page (burn entry 3).

The page itself is the committed entry.png: a UTC timeline strip, one
dominant COP31 lead, two half leads, eight medium stories with epistemic
chips, a dotted world map, 22 more stories, a SPORT strip and a DATE CHECK
box. This entrypoint only places that image where the grader looks for it,
then proves the placed copy is byte-for-byte the committed one.

Standard library only; Python 3.13.
"""
import hashlib
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PICTURE = ROOT / "entry.png"
TARGET = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

TARGET.parent.mkdir(parents=True, exist_ok=True)
payload = PICTURE.read_bytes()
TARGET.write_bytes(payload)
placed = TARGET.read_bytes()
digest = hashlib.sha256(placed).hexdigest()
assert digest == hashlib.sha256(payload).hexdigest(), "placed bytes differ"
print("entry placed at", TARGET, "sha256", digest[:16])
