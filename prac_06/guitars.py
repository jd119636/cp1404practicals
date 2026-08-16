from prac_06.guitar import Guitar

guitars = []
print("My Guitars:")

name = input("Name:")
while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    first_guitar = Guitar(name, year, cost)
    guitars.append(first_guitar)
    print(f"{first_guitar} added.")
    name = input("Name:")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "Is vintage"
    # print(guitar)
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
