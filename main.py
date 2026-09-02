"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "b5dDFSmvUfqtlAq3q+m7OUR1nq8TNwXi",
    "dJG801ttNsFp8vq5Po9Tt4X6McQI5EJw",
    "F+el/a/P9RivxDA/7PnEHQi9sKFhNyPx",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
