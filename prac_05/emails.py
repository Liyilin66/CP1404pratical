users = {}

while True:
    email = input("Email: ").strip()

    if email != "":
        # Extract name from email
        username = email.split('@')[0]
        name_parts = username.split('.')
        capitalized_name = ' '.join(part.title() for part in name_parts)

        confirmed = input(f"Is your name {capitalized_name}? (Y/n) ").strip().lower()

        if confirmed == "y" or confirmed == "":
            name = capitalized_name
        elif confirmed == "n":
            name = input("Name: ").strip()
        else:
            print("Invalid input. Assuming default (Y/Yes).")
            name = capitalized_name

        users[email] = name
    else:
        break

print("\nUsers:")
for email, name in users.items():
    print(f"{name} ({email})")
