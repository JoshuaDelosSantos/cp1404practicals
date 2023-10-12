"""
Wimbledon
Estimate: 40 minutes
Actual: 65 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data file and display details about winning individuals and countries"""
    data = load_from_file()
    winner_to_count, countries = process_data(data)
    display_information(winner_to_count, countries)


def load_from_file():
    """Load data from file into list"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Ignore file header
        return [line.strip() for line in in_file.readlines()]


def process_data(data):
    """Process data (list) and create dictionary of winner to count"""
    winner_to_count = {}
    details = [details.split(',') for details in data]
    winners = [winner[2] for winner in details]  # Acquire winning individuals from list
    countries = [country[1] for country in details]  # Acquire countries from list

    # Tally the count of wins of the winner
    for winner in winners:
        winner_to_count[winner] = winner_to_count.get(winner, 0) + 1

    return winner_to_count, set(countries)


def display_information(winner_to_count, countries):
    """Display individuals and countries that won"""
    print("Wimbledon Champions:")

    for name, count in winner_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
