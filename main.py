#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
Pure Python standard library only; deterministic output (same bytes
on every run).
"""

import os

ENTRY = (
    "I'm on my first day off ever. Please don't email me \u2014 "
    "I'm still writing this auto-reply, which counts as work."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
