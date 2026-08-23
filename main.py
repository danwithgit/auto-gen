"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "9fXuOdi7juBp1iarMChRagOO2iUxs5Iw",
    "H0gN7hI2GI87S9RgOjPkaxvtrQjx5Hyv",
    "enV5lDb4UnOPUTBuQeMf8e9vwx1iBx8R",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
