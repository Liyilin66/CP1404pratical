import random

NUM_QUICK_PICKS = 5
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PER_QUICK_PICK = 6

try:
    num_quick_picks = int(input("How many quick picks?  "))
    for _ in range(num_quick_picks):
        # Generate a list of all possible numbers
        all_numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))

        # Shuffle the list to randomize
        random.shuffle(all_numbers)

        # Select the first NUM_PER_QUICK_PICK numbers (sorted)
        quick_pick = sorted(all_numbers[:NUM_PER_QUICK_PICK])

        # Print the quick pick
        print(" ".join(f"{num:2}" for num in quick_pick))

except ValueError:
    print("Please enter a valid number.")
