from itertools import combinations_with_replacement


def findPairs(lst, K,n):
    return [pair for pair in combinations_with_replacement(lst, n) if sum(pair) == K]



# Driver code

lst=[1,2,5,10,20,50]

K = 100
sum1 = 0
for i in range (1, K+1):
    sum1 += len(findPairs(lst,K,i))
    # print(findPairs(lst,K,i))

print(sum1, "dfgjfghjds")

