"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "ki8iVCnBRZ2r2zlelkpXUmpi5rfTSuIl",
    "19nxKkzoFysMQB79swv96gBXKbJIkqpE",
    "IvMQ1MHoG7uhlfPspOQ8cGOH8oAmgCg3",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
