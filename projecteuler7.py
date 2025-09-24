count = 0
bound = 10001


def is_prime(num):
    divisor = 1
    while divisor < 1000:
        if num % divisor == 0 and divisor != num and divisor != 1:
            return False
        divisor += 1

    return True


checkNum = 1
while count < bound:
    checkNum += 1
    if is_prime(checkNum):
        count += 1

print(checkNum)