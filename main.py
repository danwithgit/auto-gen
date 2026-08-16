"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "GpwZAdGvsdBs5Z9GUI9/2+SNbnT94b88",
    "RkFqauSQgY8vy//bRXOOcsi+CCL+BqEb",
    "B8CWNvjoMRVWOHWZOeDZl6nu9LCsE5lO",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
