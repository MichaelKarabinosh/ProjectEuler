num_to_words_ones = {
    0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
     6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
     11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
     15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
}

num_to_words_tens = {0: '', 10: 'Ten', 20: 'Twenty', 30:'Thirty', 40: 'Forty',
              50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
              80: 'Eighty', 90: 'Ninety', 100: 'Hundred'}


def count_letters(num):
    if num<20:
        return len(num_to_words_ones[num])
    elif num<100:
        remainder = num % 10
        return len(num_to_words_tens[num - remainder]) + len(num_to_words_ones[remainder])
    elif num==1000:
        return len("one thousand")
    else:
        remainder_ones = num % 10
        remainder_tens = num % 100
        num_hundreds = int(num / 100)
        sum2 = len(num_to_words_ones[num_hundreds]) + len(num_to_words_tens[100]) + len(num_to_words_tens[remainder_tens - remainder_ones]) + len(num_to_words_ones[remainder_ones])
        if 10 <= remainder_tens <= 19:
            sum2 = len(num_to_words_ones[num_hundreds]) + len(num_to_words_tens[100]) + len(num_to_words_ones[remainder_tens])
        if remainder_tens >=1:
            return 3 + sum2
        else:
            return sum2




total = 0
for i in range(1,1001):
    total += count_letters(i)
    print(count_letters(i), i)

print(total)
print(count_letters(342))
print(count_letters(115))


