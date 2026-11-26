#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table.

The line is fixed and deterministic: no randomness, no input, no
network. It is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling
back to ``/output``), exactly as the brief requires: one sentence,
at most 200 characters, in the cat's own voice, no apology and no
confession.
"""

import os

# The cat's defence. One sentence, spoken, no remorse: the glass
# filed a noise complaint about the 3am zoomies, so the cat settled
# the matter the only way a cat knows how.
ENTRY = (
    "It filed a noise complaint about my 3am zoomies, so I settled "
    "it out of court \u2014 the floor was the settlement."
)


def entry_text():
    """Return the entry sentence, stripped of any stray whitespace."""
    return ENTRY.strip()


def output_path():
    """Resolve the output directory from the environment."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    """Write the entry sentence to entry.txt."""
    text = entry_text()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
