

def series_sum(n):
    from itertools import count
    sum = 0
    if n < 1:
        return '0.00'
    for i in count(1):
        sum += 1.0 / (3*i - 2)
        if i == n:
            return '{:.2f}'.format(sum)

print series_sum(1)

print series_sum(2)

print series_sum(5)
