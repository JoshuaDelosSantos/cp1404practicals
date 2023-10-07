"""
Wimbledon
Estimate: 40 minutes
Actual: 65 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_from_file()
    winner_to_count, unique_winning_countries = process_data(data)
    display_information(winner_to_count, unique_winning_countries)


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


def display_information(winner_to_count, unique_winning_countries):
    print("Wimbledon Champions:")
    for winner in winner_to_count:
        print(f"{winner} {winner_to_count[winner]}")
    print(f"\nThese {len(unique_winning_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(unique_winning_countries)))


main()
