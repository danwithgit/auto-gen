"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "5SsrCbHYKqykju7HEmaYZ2/DYZ/BtKyM",
    "PSDTU0Ha4uxq14yCEWYqkwLpYG7EaP6x",
    "04gVkKVVYszQF7vcLn1/dk/zCdUPsfc0",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
