"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "EYh/aQiLxae8U6xd5CL++CVqmK0jGEOZ",
    "rfxl0wwheHbqcVp5b1eYc0azK56KX2GM",
    "2U973A6/EYmqBPhM2AhimMCo+ecB//8x",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
