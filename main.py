"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "rUeMfvZneQQDLpmjYIgtoBZjgIpPp5oJ",
    "7NP+J1DJRKQXDPdh0GcCpkaHL/8u6/XO",
    "JwmB/ckn9KdkTq9JkQDM0KiBpAnAxBy1",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
