"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

import random

# Constants
MAX_INCREASE = 0.175  
MAX_DECREASE = 0.05
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "w.txt"

# Initialize price and day counter
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Print starting price to console
print(f"Starting price: ${price:,.2f}")

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Determine price change direction and magnitude
    if random.randint(1, 2) == 1:
        # Price increase
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decrease
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Apply price change
    price *= (1 + price_change)

    # Print the price for the current day to console
    print(f"On day {number_of_days} price is: ${price:,.2f}")

# Write the final price to the file
print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()