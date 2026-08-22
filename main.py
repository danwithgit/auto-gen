"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "oGiRtUjCt4+9xgCpEUjwyIpBEZD+Sjk3",
    "hoYj9BYmTXOmG169fxkaCEl7VXxVF0DX",
    "7LtQnXC6saXykycdLtE1SK1qeNoMKmbp",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
