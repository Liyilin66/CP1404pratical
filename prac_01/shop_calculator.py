"""
get items_number

total_price = 0

for i in range
    get price
    total_price += price

if total_price > 100
    discount = total_price * 0.1
    total_price -= discount

display all
"""
# Prompt the user to enter the number of items
items_number = int(input("Number of items: "))

# Prompt the user to enter the number of items
total_price = 0

# Loop to get the price of each item
for i in range(items_number):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {items_number} items is ${total_price:.2f}")
