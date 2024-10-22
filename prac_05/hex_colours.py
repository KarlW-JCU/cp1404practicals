"""Hex colours program."""

COLOUR_TO_HEX = {"ForestGreen": '#228b22', "RoyalBlue": '#4169e1', "RussianViolet": '#32174d',
                 "NavyBlue": '#000080', "DarkOrchid": '#9932cc', "CandyAppleRed": '#ff0800',
                 "Burgundy": '#800020', "Bistre": '#3d2b1f', "Amber": '#ffbf00',
                 "Lemon": '#fff700', "MidnightBlue": '#191970', "PersianIndigo": '#32127a'}

print(f"Colours: {list(COLOUR_TO_HEX.keys())}")
colour_to_hex_lower = {key.lower(): COLOUR_TO_HEX[key] for key in COLOUR_TO_HEX.keys()}

colour = input("Select Colour: ").lower().replace(" ", "")
while colour != "":
    try:
        print(f"Hex: {colour_to_hex_lower[colour]}")  # ignore pycharm warning
    except KeyError:
        print("Colour Not Found.")
    colour = input("Select Colour: ").lower().replace(" ", "")
