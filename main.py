"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "25bpR5JJ5vCkfNswOdt/mKn0PfvDj9LQ",
    "fB0AS3oYV1aLDq4hoGDBIc5zVuJ6BULg",
    "3ssnqF8b8zy1swPRxjzLoVAa9kDtByjG",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
