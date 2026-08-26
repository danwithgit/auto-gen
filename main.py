"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "cPhWVlQ+2rw3ZTkpF6jnRyHanEgx0v1m",
    "eJpuFqchFmdkCpgvkk3oFQ1MSD7AD3SS",
    "srIQ0T327VrWztg97CmPmuFsGk2AI+AR",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
