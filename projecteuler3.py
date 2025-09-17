num = 600851475143

bound = 1000000

numTry = 1
max = 0





def is_prime(num):
    numTry = 2
    while numTry < bound:
        if num % numTry == 0 and numTry != num:
            return False
        numTry = numTry + 1
    return True


numTry2 = 1
while numTry2 < bound:
    if num % numTry2 == 0 and is_prime(numTry2):
        max = numTry2
    numTry2 = numTry2 + 1
print(max)


