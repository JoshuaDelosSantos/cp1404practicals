COLOUR_TO_HEXADECIMAL = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Cardinal": "#c41e3a",
                         "Dandelion": "#f0e130", "Ebony": "#555d50", "Fawn": "#e5aa70", "Ginger": "#b06500",
                         "Heliotrope": "#df73ff", "Iceberg": "#71a6d2", "Inchworm": "#b2ec5d"}

colour_name = input("Enter a colour: ").title()
while colour_name != "":
    try:
        print(f"{COLOUR_TO_HEXADECIMAL[colour_name]}")
    except KeyError:
        print("That colour is not in the dictionary yet!")

    colour_name = input("Enter a colour: ").title()

print("Finished.")
