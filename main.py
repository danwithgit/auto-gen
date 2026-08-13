"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "y8wFiVOz3NGTWVUaCI9VkYx1wAA83epE",
    "I7ySAviiGpnI3rI6L1BTgxIlIS+ZLi57",
    "cJQfEZReQ1odSjgW0gT/NzKoS1V3hOoR",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
