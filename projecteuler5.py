def is_divisble(bound, num):
    test = 1
    while test < bound:
        if num % test != 0:
            return False
        test = test + 1
    return True


num = 1
num_found = False
while num < 10000000000 and num_found == False:
     if is_divisble(20,num):
        num_found = True
     num = num + 1


print(num - 1)



