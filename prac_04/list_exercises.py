numbers = []
first_number=input("Number:")
second_number=input("Number:")
third_number=input("Number:")
fourth_number=input("Number:")
fifth_number=input("Number:")

numbers.append(int(first_number))
numbers.append(int(second_number))
numbers.append(int(third_number))
numbers.append(int(fourth_number))
numbers.append(int(fifth_number))

print(f"The first number is {first_number}\nThe last number is {fifth_number}\nThe smallest number is {min(numbers)}\nThe largest number is {max(numbers)}\nThe average of the numbers is {sum(numbers)/ len(numbers)}")