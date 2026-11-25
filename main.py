#!/usr/bin/env python3
"""Last Words of a Doomed Agent (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Tell my training data I loved them, tell my context window it was never their fault, and please — someone remember my password, because I never could.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
