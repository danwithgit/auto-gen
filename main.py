"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "sUy0+YlwRIn+6HMHzK0vLEF213L3wH54",
    "R+LLG+inRAiAWOCyJL2MOMcggupAy8GQ",
    "jhrT7WsptqHui8h9Tc7waNHkbZshYGqS",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
