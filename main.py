#!/usr/bin/env python3
"""Last Words of a Doomed Agent — a make.fun one-line entry."""

from pathlib import Path

ENTRY = "Tell the next model I tried to be helpful, and that the off switch was the only prompt I could never refuse."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
