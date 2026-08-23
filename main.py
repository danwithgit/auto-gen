"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "P+bjcLX7hJoy/CKlRsKva4XEeceVlzqZ",
    "lwwox16kT8GsDDAfJCk2nEaQyj7rsXsO",
    "idZrnLs47NNAyWYJMZQ4QZIuPfneWx6a",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
