"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "lEwXpowiaB+/Od83whas7/FZxkwtdZtn",
    "QJoEsVaJlpqjVit6SEwqmaRX5rlSsy1h",
    "Png/verRYS3E0UM1OoyzrthajVZGj7AC",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
