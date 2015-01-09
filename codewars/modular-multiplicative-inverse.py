
def inverseMod(a, n):
    t, newt, r, newr = 0, 1, n, a
    while newr != 0:
        qutient = r // newr
        t, newt = newt, t - qutient * newt
        r, newr = newr, r - qutient * newr
    if r > 1:
        return 'a is not invertible' # None
    if t < 0:
        t += n
    return t

print(inverseMod(48, 101))
