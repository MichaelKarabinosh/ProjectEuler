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
    if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
        found = True
        break
    a_bound += 1
    b_bound = a_bound
    c_bound = c_bound
    while b_bound < sum_bound and not found:
        if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
            found = True
            break
        b_bound += 1
        c_bound = 0
        while c_bound < sum_bound and not found:
            if check_triplet(a_bound, b_bound, c_bound) and a_bound + b_bound + c_bound == sum_bound:
                found = True
                break
            c_bound += 1

print(a_bound, b_bound, c_bound, found)
print(a_bound * b_bound * c_bound)
