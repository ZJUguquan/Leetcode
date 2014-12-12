def getNumber(number):
    """This method should return the single value"""
    if number % 15 ==  0 :
        return 'BOTH'
    elif number % 5 == 0:
        return 'FIVE'
    elif number % 3 == 0:
        return 'THREE'
    return number

def getNumberRange(first, last):
    """This method should return a list of values"""
    res = [];
    loop = range(first, last+1) if last > first else range(first, last-1, -1)
    for i in  loop:
        res.append(getNumber(i))
    return res


print(getNumber(13))

print(getNumberRange(1,-15))