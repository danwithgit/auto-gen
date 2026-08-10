"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "lmpU3yWGY2hv+740f7qNIHmLAsOB5GJM",
    "HllC8u8uQmXEzLtdPlBVo1hGwiGJjssO",
    "nMAmCBYbGCjN+j4qL8TB7gEB5UfkguC3",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
