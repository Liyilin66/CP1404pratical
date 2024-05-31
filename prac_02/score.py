"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# The main function is responsible for obtaining the score entered by the user, calling the related function to
# calculate the result, and output the result
def main():
    score = float(input("Enter score: "))
    result = score_level(score)
    print(result)
    random_number = random_score()
    random_result = score_level(random_number)
    print(f"Random score is {random_number}, which is {random_result}")


# Return the corresponding grade according to the score
def score_level(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 > score >= 0:
        return "Bad"
    elif 90 >= score >= 50:
        return "Passable"
    else:
        return "Excellent"


# Generate a random integer between 0 and 100
def random_score():
    return random.randint(0, 100)


main()
