"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "40nc6+ZR1b7veQQmlNn5rjErr3CRmwPg",
    "QtkMn7KmRlhN2n5E/KnbrPs35dI3XXiQ",
    "ffSBScG6U3/DAspymXXQDvy6bhRIqbmW",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
