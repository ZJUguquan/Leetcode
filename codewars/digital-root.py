def digital_root(n):
    # ...
    def digitsum(s):
        s = str(s)
        return sum([int(i) for i in s]) if int(s) > 9 else s
    return digital_root(digitsum(n)) if n > 9 else n

print(digital_root(942))


'better solution'

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))