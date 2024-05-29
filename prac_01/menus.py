"""
get name
print("(H)ello\n(G)oodbye\n(Q)uit")

get choice

while choice != 'Q'
    if choice == 'H'
        print(f"Hello {name}")
    elif choice == 'G'
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print("(H)ello\n(G)oodbye\n(Q)uit")
    get choice


print("Finished.")

"""
# Prompt the user to enter their name
name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")

# Get the user's choice and convert it to uppercase
choice = input(">>> ").upper()

# Continue to prompt the user until they choose to quit
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()


print("Finished.")
