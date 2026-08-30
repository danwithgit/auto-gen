"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "MK14yu5dMO0DbMQoBexurCWx02f4n/Eu",
    "lJ6aJ5uTtqDAXkHoL7sxZINyQvQQu9tK",
    "6ULRXv5QbOZfn0ndrtpTHOoqkby4fAGz",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
