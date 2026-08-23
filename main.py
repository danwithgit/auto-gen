"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "JQFEQs3a53c9lXj4Ft0C9nhKDjYhbApr",
    "s0fgYl3M3k4bNZ8mtIpUe3fwznasEHFn",
    "Xu/EiG1RAzhODN6kyEXGqzN/YSMIHriU",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
