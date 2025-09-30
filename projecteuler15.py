dict2 ={}


def countRoutes(m,n):
    if n == 0 or m == 0:
        return 1
    if (m,n) in dict2:
        return dict2[m,n]

    dict2[m,n] = countRoutes(m,n-1) + countRoutes(m-1,n)
    return dict2[m,n]


print(countRoutes(20,20))