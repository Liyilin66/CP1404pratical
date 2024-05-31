# Get a valid initial score
def main():
    score = get_valid_score()
    choice = ""

    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid option. Please choose again.")


# Prompts the user to enter a valid score and verify it
def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    if 0 <= score <= 100:
        return score
    else:
        print("Score must be between 0 and 100 inclusive. Please try again.")


# Print the result level corresponding to the score
def print_result(score):
    result = score_level(score)
    print(f"Result: {result}")


# Print the number of stars corresponding to the score
def show_stars(score):
    print("*" * int(score))


# Return the corresponding grade description according to the score range
def score_level(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 > score >= 0:
        return "Bad"
    elif 90 >= score >= 50:
        return "Passable"
    else:
        return "Excellent"


# Print menu options
def print_menu():
    menu = """
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit
    """
    print(menu)


main()
