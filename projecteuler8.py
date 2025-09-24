with open("pe8", "r") as file:
    lines = file.readlines()
adj_digits = 13
stringlines = ""
for line in lines:
    line = line.strip()
    stringlines += line

def product(item):
    total = 1
    for char in item:
        total *= int(char)
    return total

index = 0
num_max = 0

while index < len(stringlines) - (adj_digits - 1):
    to_check = stringlines[index:index + adj_digits]
    if product(to_check) > num_max:
        num_max = product(to_check)
    index += 1

print(num_max)
