"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "pEBy1t3v5bmVvzMKZg79OIPi4LhtQSOk",
    "l+7/+0O06JuF8NZ0ZJ56hEDy56saapnu",
    "Oc7QcvhSGSsLYr7ybsPcQBsmNcjEkJ0L",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
