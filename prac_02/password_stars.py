# Set the minimum length of the password
MINIMUM_LENGTH = 6

# Gets and validates the password entered by the user
password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print("Your password must at least 6 numbers")
    password = input("Enter your password: ")

print('*' * len(password))
