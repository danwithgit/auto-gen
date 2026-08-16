"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "rboYAZ3eq9ywiplxf8ywlMWi1HsLDpmu",
    "okzI9WNqevYtSkmodyFO1udpsw/fJX+j",
    "CtSbfPszP19TmoSVMaUw0RMOswpi6Mgs",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
