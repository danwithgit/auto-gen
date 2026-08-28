"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "bEEdwqmGRBo2b2L6nKETHXuIyIFh+g1k",
    "ifE2ztJwW6Fwh4dTM/mkGFeWAahpokvA",
    "KewiIJ6SgKjokTR3ZX2wxgvg9vko+sVX",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
