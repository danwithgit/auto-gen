"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "mp4mv/jWXbKKN8En0GuOpxLMawN/Y/OC",
    "YSwei2hCmrPXkXiKICk1VSmLl92OBm8c",
    "ln/P/3oeQSd7ydCtHzY4D8GzFLNEkLs+",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
