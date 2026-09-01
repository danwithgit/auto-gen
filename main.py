"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "B1pIGzfFBwpihxquUoG2NADKUqt2Cx/9",
    "NGI4ATxbJeJnqrHqKYckbhYBnvr0LS8l",
    "oFIomNZd5uND+kSjkqX8kMWbuZBqwuW+",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
