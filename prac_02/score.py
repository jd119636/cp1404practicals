"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    # score_result = calculate_result(score)
    # random_result = calculate_result(random_score)
    print(f"User score is: {calculate_result(score)}")
    print(f"Random: {random_score} = {calculate_result(random_score)}")


def calculate_result(score):
    """Calculates the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent\nyou get a prize"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
