"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "J5CzFDVjPG0xovJ+bEF+QcEQv4KoQY37",
    "jwve8gJuN1/1WVuzKGPPzVs7nYwyDNky",
    "lxH0dthD3+JhHcIpBE6HgwMUbSgUTHgo",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
