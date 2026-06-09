
name = input("Enter your name:")
FILENAME = "name.txt"

out_file = open(FILENAME, 'w')
print(name, file = out_file)
out_file.close()

in_file = open(FILENAME,'r')
for line in in_file:
    print(f"Hi {line}")
in_file.close()

with open("numbers.txt", 'r') as in_file:
    line_1 = in_file.readline()
    line_2 = in_file.readline()
    result = int(line_1)+int(line_2)
    print(result)

with open("numbers.txt", 'r') as in_file:
    lines = in_file.readlines()[:-1]
    result= int(lines[0])+int(lines[1])
    print(result)