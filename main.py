"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "2Q8aoP7sp9ev2Hj5pyBnrXJILdbapL5z",
    "yD2klydbRiZaQ9G/hPhKStU8gpLfsv1l",
    "jo8T/iVaTW6qp9q3zqg+pYaU69CV364f",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
