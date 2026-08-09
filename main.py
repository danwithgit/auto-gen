"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "9ngnMrpAEq/4efcJL4IIXLXiIuLGShqu",
    "WackdF2EMZABK5XN3gjpdixLbTszZOdN",
    "jdUu9LX2dKvlB8JDZeGFANm82M/ZSL4e",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
