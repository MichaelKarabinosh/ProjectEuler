def is_divisble(bound, num):
    test = 1
    while test < bound:
        if (num % test != 0):
            return False
        test = test + 1
    return True


num = 1

while num < 100000000:
     if is_divisble(20,num):
         print(num)
     num = num + 1