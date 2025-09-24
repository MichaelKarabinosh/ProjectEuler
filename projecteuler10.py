import math
import sys

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227]
#
#
# while count < bound:
#     failed = False
#     for prime in primes:
#         if count % prime == 0:
#             failed = True
#             break
#     if not failed:
#         total += count
#     count += 1
# print(total)
# count = 0
# total = 2

bound = 2000000
count = 3
failed = False
total = 2
primes = [2]
while count < bound:
    percent = count / bound * 100
    sys.stdout.write(f"\r{percent:.1f}% Done")
    sys.stdout.flush() # nice looking progress viewer
    failed = False
    for prime in primes:
        if count % prime == 0:
            failed = True
            break
        if prime > math.sqrt(count): # method to check primes by dividing it by all smaller primes up to sqrt(x)
            break
    if not failed:
        primes.append(count)
        total += count
    count += 1

print("\n" + str(total))
