"""Print the Base64 values generated for this revision."""

import time

BASE64_VALUES = [
    "OAySfbj1k2vp0OrV5GQBWvU2plLhN2/p",
    "yTddUZCB1NcHSqt8G4wLQN3rhEV9YKaY",
    "cCO6z/rOG4cOnMlcrOZvxThemkFgM3Pf",
]
PRINT_INTERVAL_SECONDS = 1


def main() -> None:
    for index, value in enumerate(BASE64_VALUES):
        print(value)
        if index < len(BASE64_VALUES) - 1:
            time.sleep(PRINT_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
