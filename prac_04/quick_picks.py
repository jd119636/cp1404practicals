import random

quick_picks= int(input("How many quick picks do you want?"))
for pick in range(quick_picks):
    for i in range(6):
        print(random.randint(1, 45), end=" ")
    print()
