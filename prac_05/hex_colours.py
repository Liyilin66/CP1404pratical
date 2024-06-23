"""
Hexadecimal Colour Code Lookup
"""

COLOUR_TO_HEX = {
    "AbsoluteZero": "#0048ba",
    "AcidGreen": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "AlizarinCrimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Apricot": "#fbceb1",
    "Aqua": "#00ffff"
}

print("Hexadecimal Colour Code Lookup")
colour_name = input("Enter colour name: ").title().replace(" ", "")
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title().replace(" ", "")

# Print all colours and their hex codes, neatly aligned
print("\nAll available colours and their hex codes:")
for name, hex_code in COLOUR_TO_HEX.items():
    print(f"{name:20} is {hex_code}")
