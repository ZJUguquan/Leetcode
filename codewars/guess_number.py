
def guess_my_number(guess, number = '123-451-2345'):


    return ''.join([ (x not in guess and x.isdigit()) and '#' or x for x in number])

print(guess_my_number('01', '123-451-234'))