#http://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python


from operator import mul

prod = lambda lst: reduce(mul, map(int, lst))



def lowest_product(input):

    if len(input) < 4:
        return "Number is too small"

    start = prod(input[:4])
    lens = len(input)
    for idx, ele in enumerate(input):
        if idx > 0 and idx <= lens-4:
            temp = prod(input[idx:idx+4])
            if temp < start:
                start = temp
    return start

print lowest_product('12341111')

