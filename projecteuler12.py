import math
import itertools

def is_triangular_number(n):
    sqrt = math.sqrt(1 + 8*n)
    sum = (-1 + sqrt)/2
    if sum == int(sum):
        return True
    else:
        return False


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
    print(mults)
    product = 1
    for i in range(len(mults)):
        product *= mults[i] + 1
    return product


def list_primes(n):
    bound = n
    count = 3
    failed = False
    primes = [2]
    while count < bound:
        failed = False
        for prime in primes:
            if count % prime == 0:
                failed = True
                break
            if prime > math.sqrt(count):  # method to check primes by dividing it by all smaller primes up to sqrt(x)
                break
        if not failed:
            primes.append(count)
        count += 1
    return primes

# cheat sheet: constant = 10 for 500 or less, constant = 5 for 600 or more, constant = 1/10 for 1000 or more, constant = 1/50 for 8000 or more, etc

known_factors = []
number_to_calc_for_factors = int(input("Input a number of factors you want to find the first triangular number for: ")) # details the first triangle number I want n factors for, here it is 6
exps_list = list_prime_factors(number_to_calc_for_factors)  # this is based on the idea that the number of factors an integer has can be found by multiplying the power of each of its prime factors + 1 together
# match number_to_calc_for_factors:
#     case _ if number_to_calc_for_factors <= 200:
#         number_to_calc_for_factors *= 10
#     case _ if number_to_calc_for_factors <= 400:
#         number_to_calc_for_factors *= 2
#     case _ if number_to_calc_for_factors <= 500:
#         number_to_calc_for_factors *= 20
#     case _ if number_to_calc_for_factors < 700:
#         number_to_calc_for_factors *= 5
#     case _ if number_to_calc_for_factors < 1100:
#         number_to_calc_for_factors *= 1/10 # observation based match formula for determining constant based on the num of factors, usually as num factors goes up, constant goes down
#     case _ if number_to_calc_for_factors < 8001:
#         number_to_calc_for_factors *= 1/50
#     case _ if number_to_calc_for_factors < 10001:
#         number_to_calc_for_factors *= 1/100
primes_list = list_primes(number_to_calc_for_factors * 11) # arbritary number usually the largest factor of our number is less than 100 times the size of the number
exps_list.sort(reverse=True) #neccessary because we know that to find the smallest number, the largest exp must be associated with the smallest prime number. so if the list is 5,5,5,2,2 then we know that one of the factors is 2^5 b/c 2 is the first prime number.
print(exps_list)
total = 1
new_total = 1
for i in range(0, len(exps_list)): # iterate through each exponent of the number we want or the prime factors of the number of factors, here is 500
    if exps_list[i] > 2: # if the exponent is greater than 2, we know that it must be assoicated with the next smallest prime number
        num_to_mult = primes_list[i] ** (exps_list[i] - 1)
        total *= num_to_mult # we know a factor of the total is the smallest next distinct prime number to the power of this exponent value - 1
        known_factors.append(str(primes_list[i]) + "*" + str(exps_list[i] - 1))
        print(total,primes_list[i],exps_list[i])
    else: # if the exponent is less than 2, we have reached the end of values we know. now we must guess the bases for the exponents of 2. i use itertools here to calculate all the possible permutations of prime numbers left up to a pretty certain bound
        n = len(exps_list) - i # how many entries each perm should have. if we have three bases with exps 2, then three perms
        primes_list_upd = primes_list[i:] # delimit primes list so we only use primes we havent already. remember this only works with distinct primes
        print(len(primes_list_upd), n)
        list_combos = list(itertools.combinations(primes_list_upd, n))# list all the perms of distinct prime numbers we have

        for combo in list_combos: # for each perm in the list of perms
            print("\n")
            subtotal =1
            for nums in range(len(combo)): # for each num in this perm
                subtotal *= combo[nums] # grab this subtotal by multing each num in this perm
                print("Brute-Forced Factors:", combo[nums])
            if is_triangular_number(subtotal * total): # if this subtotal * the factor we know must be part of the num (from earlier) is a tri-number, we have found it.
                new_total = subtotal * total # we have found our product, we can break
                break
        break
if new_total == 1:
    new_total = total
print("Obvious Factors:", known_factors)
print("THE NUMBER IS:", new_total)
# print(exps_list)
# print(list_primes(500))

print("| IS TRIANGULAR NUMBER:", is_triangular_number(new_total))
print("CHECKING THIS NUMBER:",count_factors(new_total),"FACTORS")





