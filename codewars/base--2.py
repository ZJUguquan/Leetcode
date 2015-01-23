def int_to_negabinary(i):
    digits = ''
    if not i:
        digits = '0'
    else:
        while i != 0:
            i, remainder = divmod(i, -2)
            if remainder < 0:
                i, remainder = i + 1, remainder + 2
            digits = str(remainder) + digits
    return digits



def negabinary_to_int(s):
    return sum([(-2) ** i for i, c in enumerate(reversed(s)) if c == '1'])



print(int_to_negabinary(3))
print(divmod(3, -2))