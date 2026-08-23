"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "QsIAy1Fr24N9ZmzjUZoqlhnJagLBWz3W",
    "FkTV9DEqbuYarzSQAyQXCG8TewD//XLt",
    "yNoFqPl9raMArJi+D+9/dfyfWbS2vl11",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
