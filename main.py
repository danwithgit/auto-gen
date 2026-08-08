"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "xuUCq6XwnzEXye6h/MQCmiFM4E9cryH8",
    "12DtUO0U0ig/236oFcUozj5A+/fg2oIG",
    "WVixozdWfsp3uMDeEfGIYsRK4PJNCFnZ",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
