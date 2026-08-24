"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "lk8rbREYPac3JlHU3vNNGILKJWGoFyAz",
    "sf9l5KkqQmrzZ6YBNXCW2Fw8fM56tfuN",
    "argwoXJFUGuVpju8KaMLEOcNmfIz+Svu",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
