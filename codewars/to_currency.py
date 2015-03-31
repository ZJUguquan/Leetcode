def to_currency(price):
    str_ = str(price)
    res = ''
    for idx, ele in enumerate(str_[::-1]):
        if idx % 3 == 0 and idx > 1 :
            res += ','
            res += ele
        else:

            res += ele
    return res[::-1]


price = 1234567
print(to_currency(price))