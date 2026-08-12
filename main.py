"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "t4XTNwtfL64PvEL5dda9um22uBVxPZEO",
    "3QlOYska1O8+H8SavdFA8dQbMfla63Ox",
    "+YbbQe5FFbqAHGCqSlZSFj4dW+S9xaYH",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
