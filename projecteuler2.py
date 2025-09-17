


sum = 0
bound = 4000000
numprev2 = 1
numprev1 = 1
num = 1
while num < bound:
    numprev2 = numprev1
    numprev1 = num
    num = numprev2 + numprev1
    print(num)
    if num % 2 == 0:
        sum = sum + num
print(sum)
