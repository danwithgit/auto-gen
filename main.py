"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "W8TPaVLsvkBJMgvqmBgm3PM1nYSZn05Q",
    "Ilub/Y+9IxHjlfGje/7lvBciyrAMgyec",
    "lUVk7uFvOiBytP9apDu1bPd3R3CCkhas",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
