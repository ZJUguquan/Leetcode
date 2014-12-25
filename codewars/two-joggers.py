'备注  fractions 有gcd'
def lcm(a, b):
    if a == b:
        return a
    m, n = min(a, b), max(a, b)
    while m % n != 0:
        m, n = n, divmod(m, n)[1]
    return a * b // n

def nbr_of_laps(x, y):
    lcmxy = lcm(x, y)
    return [lcmxy // x, lcmxy // y]

x = [[5, 3], [4, 6]]
for i in x:
    print(nbr_of_laps(i[0], i[1]))
