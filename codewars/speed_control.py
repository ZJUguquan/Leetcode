def gps(s, x):
    # your code
    l = len(x)

    spds = [60 * 60 / float(s) * (x[i + 1] - x[i]) for i in range(l - 1)]
    if len(spds) < 1:
        return 0
    return int(max(spds))
