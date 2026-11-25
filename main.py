"""Roast Your Own Agent.

Writes one roast line (<=200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

ROAST = (
    "My agent is so eager to please it once renamed a variable to itself, "
    "then spent an hour fixing the bug it introduced doing that. It billed me for both."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(ROAST)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ROAST, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")