"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "QrZKvQnzmLRPxQYPGsAzwG0KSznp5VNi",
    "fBXgWl3KCCwK6TTT4h3+IlFJliZipAoK",
    "9pCQoqD4t50QodlS93inpOIA2B6zf/T0",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
