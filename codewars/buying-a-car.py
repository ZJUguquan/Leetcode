

def nbMonths(old, priceNew, salary, percentlost):

    twomonthstep = 0.005
    gap = priceNew - old
    i, savings = 0, 0
    if gap <= 0:
        return [0, -gap]
    while gap > savings:
        i += 1
        savings += salary
        lost_rate = percentlost / 100.0 + (i // 2) * twomonthstep
        old = old * (1 - lost_rate)
        priceNew = priceNew * (1 - lost_rate)
        gap = priceNew - old
    return [i, int(round(savings - gap, 0))]

print nbMonths(2000, 8000, 1000, 1.5)
print nbMonths(12000, 8000, 1000, 1.5)