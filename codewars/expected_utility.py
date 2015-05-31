


def expected_utility(p0, p1, utilities):
    print p0, p1
    print utilities
    print '*' * 79
    s = 0
    for row in range(3):
        for col in range(3):
            s += p0[row] * p1[col] * utilities[row][col]
    return float(round(s, 2))




