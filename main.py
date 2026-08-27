"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "AqSDgxiD27GRZnf5bqnzbPOb/6hrULZq",
    "vplA4BJlD1732q6lWSjpCsgaFJoxfFJe",
    "TLV83Jdd4LY5WgOy8KvGkNBGqWrvzxzL",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
