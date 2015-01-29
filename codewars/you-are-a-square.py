def is_square(n):
    from math import sqrt, floor
    return True if  n >= 0 and sqrt(n) == floor(sqrt(n)) else False


print(is_square(100))
