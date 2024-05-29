"""
get sales
while sales >= 0
    if sales < 1000
       bonus = sales * 0.1
    else
       bonus = sales * 0.15
    print bonus
    get sales
do next thing
"""
# Constants for bonus calculation
EDGE_NUMBER = 1000
LOW_BONUS = 0.1
HIGH_BONUS = 0.15

sales = float(input("Enter sales: $"))


while sales >= 0:
    if sales < EDGE_NUMBER:
        bonus = sales * LOW_BONUS
    else:
        bonus = sales * HIGH_BONUS

    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("ended.")
