"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "Uk9DKOX9Fo6fJdQWvoN5keb1uU7+xVSy",
    "I/LGi6KWLhVXn2XNWib0lc6fXBelrJsa",
    "+QtYs3D/spB25WevoGdwXtcMA5bI4iGP",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
