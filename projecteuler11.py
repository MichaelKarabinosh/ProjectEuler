with open("pe11", "r") as file:
    lines = file.readlines()
    nums = []
    for line in lines:
        num = line.split(" ")
        for digit in num:
            nums.append(int(digit))

index = 0
product = 0
max = 0
# while index < len(nums):
#     product = nums[index] * nums[index + 21] * nums[index + 42] * nums[index + 63]
#     index += 1
#     if product > max:
#         max = product
#     print(max)

