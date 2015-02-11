

# http://www.codewars.com/kata/union-of-intervals


def union_interval(intervals, interval):
    il = interval
    for idx, i in enumerate(intervals):
        if i[1] < il[0]:
            continue
        else:
            if i[0] < il[0]:
                il[0] = i[0]
                il[1] = max(i[1], i[1])
                intervals.pop(idx)
            else:
                if i[0] > il[1]:
                    continue
                else:
                    il[0] = min(il[0], i[0])
                    il[1] = max(i[1], i[1])
                    intervals.pop(idx)
    intervals.insert(interval)
    return intervals


print(union_interval([(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8)))

