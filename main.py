"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "f6kglrvCmCWoZQEhFD5bo3RZ3X+c1cNo",
    "XMlhHey6UL7uXoO7/PcpZCcgpQ5lG/tj",
    "V8juthtmdBOafkeosLxRcqIVIpzlykBP",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
