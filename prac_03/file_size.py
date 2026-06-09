file_name = input("Please input a filename:")
while file_name !="":
    amount_of_lines = 0
    try:
        in_file = open(file_name,'r')
    except FileNotFoundError:
        print("Error does not exist")
        file_name = input("Please input a filename:")
        continue
    for line in in_file:
        amount_of_lines+=1
    in_file.close()
    print(amount_of_lines)
    file_name = input("Please input a filename:")
print("Fin")
