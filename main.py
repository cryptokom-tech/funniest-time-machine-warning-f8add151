#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the warning label printed on a time machine. The label warns you
not to press the red button — and then informs you that you already
pressed it, which is why you are reading the label at all. A closed
causal loop, delivered with a straight face.
"""

import os
import sys

ENTRY = "WARNING: Do not press the red button. You pressed it. That is why you are reading this."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    if not (1 <= len(text) <= 120) or not text.strip():
        print("entry fails the 1-120 character gate", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the entry"
    assert 1 <= len(written) <= 120, "entry.txt fails the 1-120 character gate"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
