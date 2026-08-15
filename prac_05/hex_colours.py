COLOURS = {"AQUA": "00ffff", "AZURE": "f0ffff", "LIME": "bfff000"}

for colour, code in COLOURS.items():
    print(f"{colour} is {code}")

colour_guess = input("Colour:").upper()
while colour_guess !="":
    try:
        print(f"{colour_guess} is {COLOURS[colour_guess]}")
    except KeyError:
        print("Invalid colour")
    colour_guess = input("Colour:").upper()
