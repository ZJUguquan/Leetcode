hould return False

# should return True
#

# should return False


def same_structure_as(alist, blist):
    if type(alist) != type([1]) and type(blist)!= type([1]):
        return True

    if type(alist) == type([1]) and type(blist) != type([1]):
        return False

    if type(blist) == type([1]) and type(alist) != type([1]):
        return False

    if type(alist) == type([1]) == type(blist):
        if len(alist) != len(blist):
            return False
        for idx, _ in enumerate(alist):
            if not same_structure_as(alist[idx], blist[idx]):
                return False
    return True

print same_structure_as([1, 1, 1], [2, 2, 2])
print same_structure_as([1, [1, 1]], [2, [2, 2]])

print same_structure_as([1, [1, 1]], [[2, 2], 2])
print same_structure_as([1, [1, 1]], [[2], 2])

print same_structure_as([[[], []]], [[[], []]])
print  same_structure_as([[[], []]], [[1, 1]])
print same_structure_as([1,'[',']'] , ['[',']',1])

# should return False

# should return True
#

# should return False


def same_structure_as(alist, blist):
    if type(alist) != type([1]) and type(blist)!= type([1]):
        return True

    if type(alist) == type([1]) and type(blist) != type([1]):
        return False

    if type(blist) == type([1]) and type(alist) != type([1]):
        return False

    if type(alist) == type([1]) == type(blist):
        if len(alist) != len(blist):
            return False
        for idx, _ in enumerate(alist):
            if not same_structure_as(alist[idx], blist[idx]):
                return False
    return True

print same_structure_as([1, 1, 1], [2, 2, 2])
print same_structure_as([1, [1, 1]], [2, [2, 2]])

print same_structure_as([1, [1, 1]], [[2, 2], 2])
print same_structure_as([1, [1, 1]], [[2], 2])

print same_structure_as([[[], []]], [[[], []]])
print  same_structure_as([[[], []]], [[1, 1]])
print same_structure_as([1,'[',']'] , ['[',']',1])