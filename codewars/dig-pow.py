def dig_pow(n, p):
    s = str(n)
    res = sum([int(s[i])**(i+p) for i in range(len(s)) ])

    return res // n if res % n == 0 else - 1

print dig_pow(89, 1)
print dig_pow(92, 1)
print dig_pow(695, 2)
print dig_pow(46288, 3)