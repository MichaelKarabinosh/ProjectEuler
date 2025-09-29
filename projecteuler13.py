with open('pe13', 'r') as file:
    lines = file.readlines()

    total = 0
    for line in lines:
        numr = int(line)
        total += numr

print(str(total)[:10])
