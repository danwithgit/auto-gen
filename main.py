"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "UB6i7mY+M/fA1WXeEoS+YmnXGoVC6nix",
    "GQuQKup7q5pzwYp7XXuwyAfAtLRx7g53",
    "tdmb/6MvMw8vrn4ctsggEBAvN+Gu3UXF",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
