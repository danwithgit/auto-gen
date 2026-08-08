"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "0jcp07G7Ed15fAKQL4QmiLAzowOAGfqI",
    "eCoU+RPQWkwzxvFiL2aDXyRr1mOQVewV",
    "v8wIqSWH4lRB/8huyZM3z8r5gcggFpKO",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
