def count_sum(num):
    total = 0
    numasltr = str(num)
    for x in range(len(numasltr)):
        total += int(numasltr[x])
    return total

total = 1
for i in range(1,100):
    total *= i
print(count_sum(total))