# 1. Write a program that asks the user for their name and writes it to a file called name.txt

name = input("Please enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2. Write a program that reads the name from name.txt and prints a greeting

file = open("name.txt", "r")
name = file.read().strip()
file.close()
print(f"Hi {name}!")

# 3. Write a program that reads the first two numbers from numbers.txt, adds them together, and prints the result

file = open("numbers.txt", "r")
first_number = int(file.readline())
second_number = int(file.readline())
file.close()
result = first_number + second_number
print(result)

# 4. Write a program that prints the total for all lines in numbers.txt

total = 0
file = open("numbers.txt", "r")
for line in file:
    total += int(line)
file.close()
print(total)
