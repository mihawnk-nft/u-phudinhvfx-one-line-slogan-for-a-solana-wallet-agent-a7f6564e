#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent. Pure stdlib, deterministic.

The slogan is a single line of at most 20 words (gate: 1-140 chars).
It names the wallet, gives it a fresh image (a brain that watches the
chain), and states its promise in plain words: spend wisely, never sleep.
"""
import os

SLOGAN = (
    "Your Solana wallet grew a brain: "
    "it watches the chain, spends wisely, and never sleeps."
)


def slogan():
    """Return the entry text (single line, no trailing newline in content)."""
    return SLOGAN


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(slogan() + "\n")


if __name__ == "__main__":
    main()
