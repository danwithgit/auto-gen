"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "FKYc9/tww5DAGdtwpOsB16BDI6bC0rrL",
    "oYL8C77QMQtSu29B45tTkFNU8b8CXskJ",
    "KRNILQNwHYmyyPKDv9JfwWp/jUGycHr3",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
