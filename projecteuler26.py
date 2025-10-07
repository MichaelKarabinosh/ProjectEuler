from decimal import Decimal,getcontext
getcontext().prec = 100


def try_vals(num):
    max = 0
    for i in range(1,120):
        if 10 ** i > num:
            check = (10**i) % num
            if check > max:
                max = check
    return max

max = 0
mult = 0
list = []
for i in range(2,1000):
    if try_vals(i) > max:
        list.append([max,mult])
        max = try_vals(i)
        mult = i
    print("num repeats: ", try_vals(i), "1/",i)
    print(Decimal(1)/Decimal(i))
print(max, mult)
list.sort(reverse=True)
print(list)
