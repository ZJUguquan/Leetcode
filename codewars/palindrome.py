def palindrom(s):
    import string
    lis = [i for i in s.lower() if i in string.ascii_lowercase]
    # print(lis)
    while len(lis) >= 2:
        if lis[0] != lis[-1]:
            return False
        else:
            lis.remove(lis[0])
            lis.pop()
    return True


s = 'Amore Roma'
s = 'beer'
s = ' Level'
print(palindrom(s))
