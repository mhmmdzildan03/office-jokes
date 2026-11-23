"""Write one office joke to /output/entry.txt.

The joke: a manager calls the office a family, an employee takes
it literally and asks for an allowance, and the company answers
with a performance improvement plan. One line, 107 characters.
"""
import os

TEXT = (
    "We're a family here, my manager said, so I asked for an allowance "
    "\u2014 and got a performance improvement plan."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
