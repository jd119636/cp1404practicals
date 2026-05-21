total_cost = 0

number_of_items = int(input("input how many items you would like to purchase:"))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("input how many items you would like to purchase:"))

for item in range(1, number_of_items + 1, 1):
    price = float(input(f"what is the price of item number {item}:$"))
    total_cost += price
if total_cost >= 100:
    total_cost = total_cost * 0.9
print(f"Total price for {number_of_items} items is ${total_cost:.2f}")
