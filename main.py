#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt. The label is a straight-faced safety notice whose
punchline lands on the last words: the classic grandfather paradox,
recast as a structural-engineering problem.
"""

import os

LABEL = "WARNING: Do not alter the past. Your grandfather is load-bearing."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main() -> None:
    # Exactly one line: no embedded newline, and the gate counts the
    # label itself (1-120 chars, not only whitespace).
    if "\n" in LABEL or "\r" in LABEL:
        raise ValueError("label must be a single line")
    if not (1 <= len(LABEL) <= MAX_CHARS) or not LABEL.strip():
        raise ValueError("label fails the 1-120 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
