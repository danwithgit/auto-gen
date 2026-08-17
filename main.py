"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "RiBE6MXGa4jvMaPLPNv07ZShlqj67kYk",
    "zpxhGsGORmYsnJEkJJH656d0gjHSH/Z7",
    "8By3Z5VG9fvOzsgSFv3pK/saR7Q5VjLA",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
