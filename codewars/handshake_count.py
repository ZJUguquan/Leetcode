



def get_participants(h=0):
    if h < 2:
        return h +1

    #n*(n- n - 2  h
    from math import floor, ceil
    if int((1+8*h)**.5) == ceil((1+8*h)**.5):
        return int( (1+(1+8*h)**.5)/2)
    return int(ceil(2 + (1+8*h)** .5)/2)


for _ in [0,1,3,6, 7]:
    print get_participants(_)