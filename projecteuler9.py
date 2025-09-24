import math


def check_triplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

a_bound = 0
b_bound = 0
c_bound = 0
found = False
sum_bound = 1000

while a_bound < sum_bound and not found:
    a_bound += 1
    b_bound = 0
    while b_bound < sum_bound and not found:
        b_bound += 1
        if ((sum_bound ** 2) - (2 * sum_bound * a_bound) - (2 * sum_bound * b_bound) + (2 * a_bound * b_bound)) == 0: # derived equation from setting c = sqrt(a^2 + b^2) equal to c = 1000 - a - b
            c_bound = int(math.sqrt(a_bound ** 2 + b_bound ** 2))
            if check_triplet(a_bound, b_bound, c_bound):
                found = True
print("Found:",found)
print(a_bound, b_bound, c_bound)
print(a_bound * b_bound * c_bound)


# while a_bound < sum_bound and not found:
#     if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
#         found = True
#         break
#     a_bound += 1
#     b_bound = a_bound
#     c_bound = c_bound
#     while b_bound < sum_bound and not found:
#         if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
#             found = True
#             break
#         b_bound += 1
#         c_bound = 0
#         while c_bound < sum_bound and not found:
#             if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
#                 found = True
#                 break
#             c_bound += 1
#
# print(a_bound, b_bound, c_bound, found)
# print(a_bound * b_bound * c_bound)
#
# a_bound = 0
# b_bound = 0
