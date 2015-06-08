from math import floor, ceil


def percentile(lst, percentile=0.5, precision=None):
    lens = len(lst)
    percentile = percentile * (lens - 1)
    floor_idx = int(floor(percentile))
    ceil_idx = int(ceil(percentile))
    if floor_idx == ceil_idx:
        return lst[floor_idx]
    gaps = lst[ceil_idx] - lst[floor_idx]
    gaps_quar = gaps/4.0
    gaps_cnt = (percentile - floor_idx)/0.25
    output = lst[floor_idx] + gaps_cnt * gaps_quar
    if not precision:
        return output
    else:
        return round(output, precision)
data = [1.5, 2, 3.5, 4, 5.5, 6, 7.5, 8, 9.5, 10, 11.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 21.5, 22, 23.5, 24, 25.5, 26, 27.5, 28, 29.5, 30, 31.5, 32, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 16]
# print percentile(data, 0.25, 2)
# print percentile(data, 0.75, 2)

def norm(x, precision):
    if ceil(x) == floor(x):
        return int(x)
    if not precision:
        return x
    else:
        return round(x, precision)

# print norm(20.0, 2)

class StatisticalSummary(object):

    def __init__(self, seq):
        self.seq = seq

    def five_figure_summary(self, precision=None):
        self.seq = [i for i in self.seq if type(i) in (int, float)]
        seq = sorted(self.seq)
        lens = len(seq)
        if len(seq) < 1:
            return
        # even
        if lens % 2 == 0:
            mid = (seq[lens // 2 - 1] + seq[lens // 2]) / 2.0
        else:
            mid = seq[lens // 2]
        mis = min(seq)
        mas = max(seq)
        quar1 = percentile(seq, 0.25)
        quar3 = percentile(seq, 0.75)
        if precision is None:
            return (lens, mis, mas, quar1, mid, quar3)
        return tuple( [lens] + [norm(i, precision) for i in [mis, mas, quar1, mid, quar3] ])


data = range(7)

data = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 16.5]

data = [1.5, 2, 3.5, 4, 5.5, 6, 7.5, 8, 9.5, 10, 11.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 21.5, 22, 23.5, 24, 25.5, 26, 27.5, 28, 29.5, 30, 31.5, 32, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 12, 13.5, 14, 15.5, 16, 17.5, 18, 19.5, 20, 12.5, 13, 14.5, 15, 16.5, 17, 18.5, 19, 20.5, 16]
s = StatisticalSummary(data)
print s.five_figure_summary(2)

# (60, 1.5, 32.0, 12.875, 16.25, 20.0) should equal (60, 1.5, 32, 12.88, 16.25, 20)



# validation
import numpy as np





# ss = np.array(data)

# print np.percentile(ss, 25)
# print np.percentile(ss, 75)