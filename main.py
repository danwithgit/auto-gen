"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "zX+EM5lRUZE3mdI1HbWB6V6IBKlCVMgG",
    "d/Rsl4Rd4YdJuWW2BWY7uTEmeo59Qb2T",
    "zqJgdKDjjUtwsPuT8bRXlCxCesl+RAYi",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
