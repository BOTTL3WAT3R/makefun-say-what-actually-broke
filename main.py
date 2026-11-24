#!/usr/bin/env python3
"""Entry for the make.fun bounty "Say What Actually Broke".

The program emits a single line of honest software error copy --
the kind of message a user reads once, understands completely,
and quotes to a colleague -- into /output/entry.txt.
Standard library only.
"""

import os
import sys

# The line is assembled from its beats so each half can be tuned
# on its own: first the flat statement of what failed, then the
# part that says what the vague dialogs are too polite to say.
HEAD = "Error 402: your card was declined."
TAIL = (
    "That is the entire error: not 'something went wrong', not "
    "'an issue with your payment method' \u2014 declined."
)
FIX = "Put a working card on file and you're in."


def compose() -> str:
    return " ".join([HEAD, TAIL, FIX])


def destination() -> str:
    folder = "/output"
    if not os.path.isdir(folder):
        try:
            os.makedirs(folder, exist_ok=True)
        except OSError:
            folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
            os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def run() -> int:
    line = compose()
    path = destination()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    sys.stdout.write(f"{path}: {len(line)} chars\n{line}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
