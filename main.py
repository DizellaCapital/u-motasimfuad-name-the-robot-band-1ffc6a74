#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Name the Robot Band".

Writes one funny robot band name plus a few words on its hit song
(1-200 characters, single line) to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to /output/entry.txt, then verifies the written bytes.
"""

import os
import sys

ENTRY = (
    "The Self-Checkouts — hit single 'Unexpected Item in the Bagging Area' "
    "has been stuck at No. 1 for six years. Nobody can remove it."
)


def validate(line: str) -> str:
    """Enforce the sealed gate from RULES: 1-200 chars, single line, not blank."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    try:
        line = validate(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != line:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(line)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
