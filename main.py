"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "BvIa7LRglqV0aHHh/UO3jNL0AmaupNZr",
    "DkUGgsj9C9UvOkxdnsBChMO72MI/I6wk",
    "NpLTIb1ctF6YrOdj6DG0nfUlxxabkC5v",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
