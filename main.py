"""Office-jokes entry for make.fun competition
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes exactly one original one-line joke about office life to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

JOKE = (
    "I hit reply-all to tell everyone to stop hitting reply-all, "
    "and now I'm the person new hires get warned about."
)


def output_path() -> str:
    """Resolve the entry file path from OUTPUT_DIR, default /output."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
