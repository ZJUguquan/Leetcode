def root(x, n):
    s = x**(1.0/n)
    if int(s) == s:
        return int(s)
    return s

print root(6.25, 2)
print root(1024, 10)