"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "SY9XukcW3nwDZqV9dgNa7sZqNPxDux16",
    "SNxp2ZpBvbTI5JkQEUxQ0Ncwm5lI+Mji",
    "Sks7IRBd5MkIARDtXFfSZgPeSWu6K4DR",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
