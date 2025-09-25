def list_divisors(num):
    divisors = []
    modulo = 1
    while modulo <= num:
        if num % modulo == 0:
            divisors.append(modulo)
        modulo += 1
    return divisors

print(list_divisors(231))
