"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "FYUCjDJXo5tmAlW4sk5lphDE0t2MJDtW",
    "6u2n3Ipo/EBVGHUixq6BOdPFz7G5lxRU",
    "DPlapI13Ax+/ShUE4sl0DfLb9avkMY8R",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
