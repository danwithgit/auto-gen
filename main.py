"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "/Cq8qt5hNy1uhAS4FWHABjtYzCxOzgBs",
    "ZdeOvEqd5EpxeLe2+uy+4OMkcXfAuRut",
    "00SVPzG5byiheYa0/elvo27a0+F9GxDQ",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
