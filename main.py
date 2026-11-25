"""invent-a-word: write the entry to /output/entry.txt.

Stdlib only. Run: python3 main.py
"""

import os
import sys

ENTRY = "nodbluff (n.): nodding along to a conversation you stopped understanding minutes ago."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate: 1-140 chars, not only whitespace, no trailing newline.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of range 1-140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify byte-identical output.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "output is not byte-identical to ENTRY"
    assert 1 <= len(raw.decode("utf-8")) <= 140, "written entry out of range"
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars)")
    print(ENTRY)

    return 0


if __name__ == "__main__":
    sys.exit(main())
