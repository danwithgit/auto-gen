"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "R3mDWpy/meaGdUZyHa/Lu8EbZhwQty6r",
    "Xw89eTsq5ImkqRhw33frld/u10625q6A",
    "X1OtT1hvsVahZyjRZ/irm5eMmLiB5bEP",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
