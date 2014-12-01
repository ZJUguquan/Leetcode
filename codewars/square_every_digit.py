def square_digits(num):
    s = str(num) ; res = ''
    for digit in s:
        digit_square = int(digit) ** 2
        res += str(digit_square)
    return int(res)



print(square_digits(9119))




def square_digits(num):
    return int(''.join([ str(int(s) **2) for s in str(num) ]))
print(square_digits(9100))
