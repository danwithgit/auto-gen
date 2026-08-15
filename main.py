"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "WTnv/p4yIfiHfUdNJIUHQyYEOscDDKjQ",
    "c0RDD6olv82DvERzXTX5GNPQ9ksgPx4s",
    "50HeRkQEiSiBaHPOs43QfuKpjYZVYP80",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
