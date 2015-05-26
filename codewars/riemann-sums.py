def xxrange(start, stop, step):

    while start < stop:
        yield start
        start += step


def left_riemann(f, n, a, b):
    sum = 0
    step = (b-a) / 10000.0
    for ss in xxrange(a, b, step):
        sum += f(ss) * step
    return  round(sum, 3)