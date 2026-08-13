"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "x40LbwkRQPAxGqUcLRdc1SGn++ii3ga6",
    "skkPDXkbRihMiM/OESZkLt6LLaqwQIeT",
    "IZ1tV2ZOhHZyIl0Ry42kWNWUYLmbokw5",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
