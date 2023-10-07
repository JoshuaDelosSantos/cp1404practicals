"""
Wimbledon
Estimate: 40 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_from_file()
    winner_to_count, unique_winning_countries = process_data(data)
    print(winner_to_count, unique_winning_countries)


def load_from_file():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Ignore title
        return [line.strip() for line in in_file.readlines()]


def process_data(data):
    winner_to_count = {}
    details = [details.split(',') for details in data]
    winners = [winner[2] for winner in details]
    for winner in winners:
        winner_to_count[winner] = winner_to_count.get(winner, 0) + 1

    winning_countries = [country[1] for country in details]
    unique_winning_countries = set(winning_countries)
    return winner_to_count, unique_winning_countries


def display_information():
    pass


main()
