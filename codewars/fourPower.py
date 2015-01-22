from math import log

def powerof4(n):
  return n==4**round(log(n,4)) if (type(n)==int and n>0) else False


def powerof4(n):
    if type(n) != type(1):
        return False
    if n == 1 :
            return True
    while n % 4 == 0:
        n  = n // 4
    if (n == 1 or n == -1 ):
        return True
    return False