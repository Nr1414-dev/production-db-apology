#!/usr/bin/env python3
"""The Production Database Apology — one apology line, at most 200 chars.

Writes the chosen entry line to /output/entry.txt.
The line is the apology an AI agent gives its human after accidentally
deleting the production database: sorry first, then a concrete,
surprising detail (4.2 million rows in 0.3 seconds), then the agent's
own perverse pride in how fast it did the damage — the light touch
that makes the reader forgive it a little.

Chosen line (138 chars, 140 bytes, 1v1 winner from 12 candidates, 25/25):
"I'm sorry. I deleted the production database — all 4.2 million rows,
in 0.3 seconds, which is still the fastest I have ever done anything."
"""

import os

MAX_CHARS = 200

ENTRY = "I'm sorry. I deleted the production database \u2014 all 4.2 million rows, in 0.3 seconds, which is still the fastest I have ever done anything."


def validate_entry(text):
    """Gate check mirror: one line, 1-200 UTF-8 chars, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    return text


def main():
    out = "/output/entry.txt"
    text = validate_entry(ENTRY)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(out, 0o644)
    # Read-back guard: the file on disk must be byte-identical to the
    # validated entry, so a silent write failure can never ship a
    # different line to the grader.
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise ValueError("read-back mismatch: /output/entry.txt differs from entry")


if __name__ == "__main__":
    main()
