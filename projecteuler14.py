
def count_terms(n, seen): # super efficient algo that stores previously found sequences in a dict, if the value has been seen we skip and add current count + the count of the value in dict
    num = n
    count = 0
    while num != 1:
        if int(num) in seen:
            seen[n] = seen[int(num)] + count
            return seen
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        count += 1
    seen[int(n)] = count
    return seen




high= 0
bound = 10000000
seen_global = {}
for i in range(1, bound):
    seen_global = count_terms(i, seen_global)


key_with_highest_value = max(seen_global, key=seen_global.get)
print("Number:", key_with_highest_value, "\nPath Length:", seen_global[key_with_highest_value])