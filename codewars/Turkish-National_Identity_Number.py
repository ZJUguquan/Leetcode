def check_valid_tr_number(number):
    # code
    if type(number) != type(1): return False
    if len(str(number)) != 11: return False

    numbers = map(int, list(str(number)))
    tenth, eleven = numbers[-2], numbers[-1]
    # sum of 1st, 3rd, 5th, 7th, 9th
    sums = sum(numbers[:-2:2])
    # multiply bt 7
    multiply7 = sums * 7
    # sum of 2 4 6 8
    sums2 = sum(numbers[1:9:2])
    substract = multiply7 - sums2
    modulus = substract % 10
    return sum(numbers[:10]) % 10 == eleven and modulus == tenth


print check_valid_tr_number(10167994524)
