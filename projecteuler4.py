def is_palindrome(num):
    plaintext = str(num)
    index = int(len(plaintext) / 2)

    half1 = plaintext[index:]
    half2 = plaintext[:index]
    if half2[::-1] == half1:
        return True
    return False

num1 = 0
num2 = 0

max = 0
while num1 < 1000:
    num1 = num1 + 1
    while num2 < 1000:
        num2 = num2 + 1
        if is_palindrome(num1 * num2) and max < (num2 * num1):
            max = num2 * num1
            maxnum2 = num2
            maxnum1 = num1
    num2 = 1
print(max, maxnum1, maxnum2)