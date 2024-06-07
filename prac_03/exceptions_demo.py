"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer:When the numerator or denominator appears to be not an integer or a sign.
2. When will a ZeroDivisionError occur?
Answer:When the number entered in the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
