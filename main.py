"""Angry Judge: The Short Rant Contest — entry writer.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The rant: the self-checkout machine — it scans the milk, weighs the
bag, and still screams "unexpected item in the bagging area" at crisps
that have not even been touched. Shared anger, concrete detail, and
the punch lands on the till having trust issues and a megaphone.
"""

import os
from pathlib import Path

ENTRY = (
    "The self-checkout scanned my milk, weighed my bag, and still "
    "screamed 'unexpected item in the bagging area' at crisps I "
    "haven't even touched. I came to buy dinner, not to be "
    "interrogated by a till with trust issues and a megaphone."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the rant's
    # UTF-8 encoding — a text-level comparison would hide a stray BOM
    # or newline the grader's character counter would still see.
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match the rant"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
