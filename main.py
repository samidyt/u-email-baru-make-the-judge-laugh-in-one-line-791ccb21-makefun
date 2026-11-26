#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — make.fun entry.

Writes a single funny line (1-200 characters) to /output/entry.txt.
Program/v1 harness, Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = "My Roomba escaped out the front door yesterday — even the robot whose whole job is bumping into walls wanted out of this house."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
