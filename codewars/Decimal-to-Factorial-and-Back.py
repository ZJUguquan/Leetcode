
# coding: utf-8

def find_duplicates(employees):
    newe = []
    output = []
    for idx, ew in enumerate(employees):
        #print ew

        e = ew.last_name + ew.user_name# + ew.first_name
        #print e
        if e not in newe:
            newe.append(e)
        else:
            output.append(ew)
            employees.pop(idx)
    return output

def o(msg=None):
    print( ('*'*30+str(msg)+'*'*30).center(80))

from math imoprt factorial


def dec2FactString(nb):
    res = ''
    maxi = 9
    while nb > 0:
        if nb // factorial(maxi) > 0:
            qu, nb = divmod(nb, r)

            maxi -= 1
        else:
            maxi -= 1