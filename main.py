"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "p+ogIPJfcCA51IGNR47N4ZDVXKM8iMzX",
    "5K1sIdZ+N+4iNXixl0gZLs5AKYHGaYt3",
    "u8XwHcebBNKxm+mO96JtGOWmGl0Zw1Zk",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
