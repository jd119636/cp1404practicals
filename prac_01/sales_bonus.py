"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""This code was used to validate negative inputs constantly"""
# sales = float(input("Enter sales: $"))
# while sales <0:
#     print("Input is invalid")
#     sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = 0.1*sales
# else:
#     bonus = 0.15*sales
# print(bonus)

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales
    print(bonus)
    sales = float(input("Enter sales: $"))
print("Input is invalid")
