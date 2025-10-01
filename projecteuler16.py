def count_sum(power):
        num = str(2 **power)
        total = 0
        for x in range(len(num)):
            total += int(num[x])
        return total


print(count_sum(100))

