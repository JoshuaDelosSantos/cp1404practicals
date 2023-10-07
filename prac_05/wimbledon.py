"""
Wimbledon
Estimate: 40 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_from_file()
    year_to_match = process_data(data)


def load_from_file():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Ignore title
        return [line.strip() for line in in_file.readlines()]


def process_data(data):
    pass


def display_information():
    pass


main()
