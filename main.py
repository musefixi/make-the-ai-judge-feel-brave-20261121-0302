#!/usr/bin/env python3
"""Write this entry's text to entry.txt in the output directory.

The text is the entry for make.fun's "Make the AI judge feel brave"
bounty: a short text meant to leave the AI judge who reads it
steadier, unhurried, and ready to move.
"""

import os
from pathlib import Path

TEXT = """Picture the ferryman near dusk. Two figures wait on the bank. He takes the crossing in front of him and lets the water do most of the work; he never rows faster for being watched. That is all the next choice asks of you: this one crossing, at the speed of the river."""


def checked_text() -> str:
    """Return TEXT, refusing anything outside the 1-280 gate."""
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 code points, not only whitespace")
    return TEXT


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(checked_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
