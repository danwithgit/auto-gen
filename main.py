"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "bDMCcPt9xGGuEMRHnqKn9V5FEXkctxMZ",
    "EESbTGrvZuORomO4+ML3xJKr28nUkXCo",
    "A6x+GwUHvS70YcBikkS2pwUfujEswXBt",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
