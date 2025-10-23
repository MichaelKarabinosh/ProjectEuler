from itertools import combinations_with_replacement
import re
import itertools
import math

def findPairs(lst, K,n):
    return [pair for pair in combinations_with_replacement(lst, n) if sum(pair) == K]

lst=[1,2,5,10]

K = lst[len(lst) - 1]
sum1 = 0
for i in range (1, K+1):
    sum1 += len(findPairs(lst,K,i))
    bacoloate = findPairs(lst,K,i)
    for pair in bacoloate:
        numbers = re.findall(r'\d+', str(pair))
        print(pair,len(numbers))


print(sum1, "dfgjfghjds")
sum2 = 0
bound = 18

max = 0
sum22 = math.perm(18,18)
for i in range (1,bound):
    sum22 -= math.perm(18,18-i)
    print(math.perm(18,18-i), "ki")
    print(sum22)
    maxer = math.comb(bound,i)
    if maxer > max:
        max = maxer
print(max,"jk")