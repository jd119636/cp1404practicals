from prac_07.guitar import Guitar

FILE_NAME = "guitars.csv"
guitars = []

with open(FILE_NAME,"r")as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        guitars.append(Guitar(name, int(year), float(cost)))

guitars.sort()
for guitar in guitars:
    print(guitar)