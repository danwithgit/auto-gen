"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "VFzUILe/OHqvJ8EpZ+AlVluk3K/lYKjd",
    "+nKerY3E9CwleS6I5oPvQiM9AiE1Ye4D",
    "5qpXq45gAnqQ4wO+HTE/bxyI1hsNe4dI",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
