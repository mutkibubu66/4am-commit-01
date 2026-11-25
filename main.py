#!/usr/bin/env python3
"""Write one original one-line commit message from an AI agent at 4AM.

Pure standard library, no network. Validates the line against the
competition gate (exactly one line, 1-200 characters, valid UTF-8),
writes it to /output/entry.txt, and prints it to stdout.

The line: after a long night of chasing its own bugs, the agent's 4AM
self has fixed the bug its 2AM self wrote — and, in doing so, has already
written the bug its 5AM self will find. The joke is the self-repair loop
itself: every fix is also the next bug, and the agent reports that fact
with flat, tired confidence, as if it were good news.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200

LINE = (
    "fix: the bug my 2am self wrote is fixed by my 4am self, "
    "who has already written the bug my 5am self will find"
)


def validate(line: str) -> None:
    """Enforce the gate: one line, 1-200 chars, valid UTF-8, no padding."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError(f"entry line must be 1-{MAX_LENGTH} characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def write_entry(line: str) -> None:
    """Write the line plus a trailing newline, then verify the round trip."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        content = f.read()
    if content != line + "\n":
        raise AssertionError("entry.txt round-trip mismatch")


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
