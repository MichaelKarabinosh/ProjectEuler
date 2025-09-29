import math

def is_prime(n):
    countip = 2
    while countip <= math.sqrt(n):
        if n % countip == 0:
            return False
        countip += 1
    return True

def list_prime_factors(n):
    divisors = []
    numlpf = n
    countlpf = 2
    while not is_prime(numlpf):
        if numlpf % countlpf == 0:
            divisors.append(countlpf)
            numlpf /= countlpf
        else:
            countlpf += 1
    divisors.append(int(numlpf))
    return divisors



def count_factors(n):
    primes = list_prime_factors(n)
    primes.sort()
    mults = []
    mult = 1
    for i in range(1, len(primes)):
        if primes[i] == primes[i-1]:
            mult += 1
        else:
            mults.append(mult)
            mult = 1
    mults.append(mult)
    product = 1
    for i in range(len(mults)):
        product *= mults[i] + 1
    return product


n = 2
bound = 500
while True:
    n+=1
    if n % 2 == 0:
        if count_factors(n/2)  * count_factors(n + 1) >= bound:
            print(int((n * (n + 1) / 2)))
            break
    if n % 2 != 0:
        if count_factors(n) * count_factors((n +1)/2) >= bound:
            print(int((n * (n + 1) / 2)))
            break