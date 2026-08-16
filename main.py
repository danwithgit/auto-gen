"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "0R/9gO6fXlalguSoBod2BLcM1SPKs8Z9",
    "n7UNKaXovQ6UZsC4Tu7XusGsurVASfKJ",
    "DGd2WaaalDPf4/jRs+M3S2zhLBBDi/9Z",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
