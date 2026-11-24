"""Entry for make.fun: "Ridiculous at First Glance, Real by the Second".

Writes a single sentence (at most 200 characters) to /output/entry.txt,
pitching a startup idea that sounds like a joke until the reader sees
who pays for it and why the business holds together.
"""

import os

PITCH = (
    "We run a five-star hotel for houseplants: globetrotting owners pay "
    "$40 a month to board their ferns, and it works because plants tip "
    "nothing, trash nothing, and never leave bad reviews."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()
