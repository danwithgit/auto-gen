"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "OhE/bZUg75FTn486+IL1UgO/v+qX522U",
    "7JYb2mFhDk9DR2suBMI9hrIMzT4f1Pag",
    "u7GyLjm+GiqTQuFHdpq8zht9bqPkBQup",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
