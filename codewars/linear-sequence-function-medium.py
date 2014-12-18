‘http://www.codewars.com/kata/54784a99b5339e1eaf000807/discuss’

def get_function(sequence):
    k = sequence[1] - sequence[0]
    b = sequence[0]
    valid = all(x == k * i + b for i, x in enumerate(sequence))
    if not valid:
    # k_list = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    # if min(k_list) != max(k_list):
        return lambda x: 'Non-linear sequence'
    return lambda x: k*x + b

# at 0x7f1308a56140> should equal 'Non-linear sequence'

print(get_function([0, 1, 2, 3, 4])(5))
print(get_function([1, 4, 7, 10, 13])(20))
print(get_function([1, 1, 1, 1, 1])(20))
print(get_function([1, 1, 1, 1, 2])(20))
# test.assert_equals(get_function([0, 1, 2, 3, 4])(5), 5, "Nope! Try again.")
# test.assert_equals(get_function([0, 3, 6, 9, 12])(10), 30, "Nope! Try again.")
# test.assert_equals(get_function([1, 4, 7, 10, 13])(20), 61, "Nope! Try again.")