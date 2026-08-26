"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "QvL6prs1gT6wvTYKCSvx5vPQAig25YHJ",
    "LK+l53P7b2Jnu7/lDjHRMyfcYvDpKxjY",
    "YhPVGeFcyZ9S9MgNB2Uny1auz41cJlKB",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
