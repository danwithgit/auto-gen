"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "AtKoUcpV0Q1LAK32XTXGk1CEP3AOIwbb",
    "1lzZoDaM3wbfs/6XTqK1sssC71lN6PWZ",
    "KjTQpDUxevDyQNXNe1gbQ2rvD2Hl6qqP",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
