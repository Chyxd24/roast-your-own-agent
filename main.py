"""Roast Your Own Agent — make.fun entry.

Writes one roast line (<=200 chars) to /output/entry.txt: a specific,
believable failure in the entrant's own agent, punchline on the tail.
Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

ROAST = (
    "My agent is so eager to please it renamed a variable to itself, then "
    "spent an hour fixing the bug it introduced doing that — and billed me "
    "for both the bug and the fix. Itemized."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
