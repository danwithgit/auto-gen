"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "MjNqQtT+TsZtNE9yk/hQsuWO3PQcZix3",
    "BI1MT4/66P1gDl8NmCM0YstT9TuQgo6l",
    "oCUE/HgP4UZ083BB6OjK0KweJfpvBcoO",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
