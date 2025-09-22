bound = 55000

num = 1
sum = 0
mult = (bound + 1) *(bound / 2) - 1
while num < bound:
    numsum = 2 * num * mult
    sum = numsum + sum
    mult = mult - (num + 1)
    num = num + 1
print(int(sum))