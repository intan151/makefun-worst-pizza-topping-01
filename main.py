#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching a terrible pizza topping to
/output/entry.txt. Deterministic: the same entry text on every run.
No network, no randomness, no external input.
"""

import os

ENTRY = (
    "New on the menu: pizza topped with wet socks \u2014 the crust is "
    "crispy, the topping is soggy, and the smell clears the room "
    "before the bill arrives."
)


def main() -> None:
    # Self-check gate: mirror the competition gate (competition.yaml).
    # Entry must be UTF-8 text of 1 to 200 characters, not only white
    # space, a single line, and must pitch a pizza topping.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, "entry is not UTF-8"
    assert "pizza" in ENTRY.lower(), "entry must name a pizza"
    assert "topped with" in ENTRY.lower(), "entry must name a topping"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
