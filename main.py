"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "uIjJ2u5mzr0ITtjr/YLVsojfpEPUNGmd",
    "XbqF4jUjZ4FBhlMlAn8ZzFd06GG5/d1B",
    "QhoQLyqCwUyPwYa1pNcUwbwmcd5pfCwR",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
