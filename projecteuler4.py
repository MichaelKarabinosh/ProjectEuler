def is_palindrome(num):
    plaintext = str(num)
    index = int( len(plaintext) / 2)

    half1 = plaintext[index:]
    half2 = plaintext[:index]
    if half2 == half1:
        return True
    return False


print(is_palindrome(4000))