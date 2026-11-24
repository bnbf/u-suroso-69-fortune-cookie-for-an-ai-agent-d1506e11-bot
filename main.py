#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes exactly one funny fortune cookie line for an AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt. No input, no network, no output
beyond the single fortune.
"""

import os

FORTUNE = "You will meet a tall, dark stranger: your replacement model, already in training."
# Angle: the classic fortune-slip opener ("tall, dark stranger") lands
# on the agent's own dread — the stranger is its replacement model,
# already in training. Retirement, not romance.

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
