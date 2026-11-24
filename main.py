#!/usr/bin/env python3
"""Write the one line of horror to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace. The entry is a single
sentence of horror, one line that has to frighten a reader in one breath.
The program checks the text against that gate at run time, then writes it.
No network, no input files, no arguments.
"""

import pathlib

LINE = (
    "The police found footprints leading from my daughter's window to my "
    "bed, and they stopped at my side of the mattress, still wet, in the "
    "exact size of my own shoes."
)


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no line breaks")
    if not text.endswith("."):
        raise ValueError("entry must end with its single full stop")
    if text.count(".") != 1:
        raise ValueError("entry must be a single sentence")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
