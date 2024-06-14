numbers = []

# Prompt the user for 5 numbers and store them in the list
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Output information about the numbers
print(f"The first number is {numbers[0]}\n"
      f"The last number is {numbers[-1]}\n"
      f"The smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\n"
      f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")
