"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "bp5xcALzP6aBbqu09RR+Fqo9Mzv4tVjm",
    "+UvvlW4gBUDhUf8n2o8eX/0p3OJ2iJEG",
    "mk5vYxHSyjWveZibLdvhAsc5ck2xhPwZ",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
