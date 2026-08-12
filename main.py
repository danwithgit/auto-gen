"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "/wnIR8JOrOhOmjRBo16cAk2QY6EWPlKS",
    "nUeSftrb2dbZJfOlfFd+8P9KH4NquvJi",
    "TcXU394oZoMaXX53uPVXDQmdmv3MLJn6",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
