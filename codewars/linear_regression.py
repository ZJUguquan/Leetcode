
def mean(x):
    return sum(x)/float(len(x))

def sums(x, y):
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    return sum_xy

def regressionLine(x, y):
    x_m = mean(x)
    y_m = mean(y)
    sum_xx = sums(x, x)
    sum_xy = sums(x, y)
    n = len(x)
    beta = (sum_xy * n - sum(x) * sum(y)) / float((n * sum_xx - sum(x) **2))
    beta1 = round(beta, 4)
    return (round(y_m - beta* x_m, 4), beta1)


