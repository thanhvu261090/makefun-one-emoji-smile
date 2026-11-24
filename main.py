#!/usr/bin/env python3
"""make.fun entry: One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt. The entry is the heart-hands
emoji: a warm, open gesture a stranger reads instantly as kindness, with no
words, no irony and nothing that needs context to land.
"""

import os
import sys

ENTRY = "\U0001FAF6"  # 🫶 heart hands

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Enforce the kit's entry gate: UTF-8 text, 1 to 8 characters,
    not only white space. This entry is a single emoji, so also reject
    control characters and require exactly one visible character."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 8:
        return False
    if text.strip() == "":
        return False
    if len(text) != 1:
        return False
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return True


def main():
    if not gate_check(ENTRY):
        print("gate check failed for entry", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %r (%d character) to %s" % (ENTRY, len(ENTRY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
