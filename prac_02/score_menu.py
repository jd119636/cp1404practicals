import random

MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result \n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("Enter your choice:").upper()
    while choice != "Q":
        if choice == "G":
            random_score = calc_score()
            print("Score generated")
        elif choice == "P":
            print_score(random_score)
        elif choice == "S":
            stars = make_stars(random_score)
            print(stars)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Enter your choice:").upper()
    print("Goodbye")


def print_score(random_score):
    print(random_score)


def calc_score():
    random_score = random.randint(0, 100)
    return random_score


def make_stars(random_score):
    stars = ("*" * random_score)
    return stars


main()
