#coding=utf-8

def interval_insert(intervals, interval):
    il = [interval[0], interval[1]]
    result = []
    for idx, i in enumerate(intervals):
        left, right = i[0], i[1]
        if left > il[1] or right < il[0]:
            result.append(i)
            continue
        else:
            if left < il[0] and right >= il[0]:
                il[0] = left
                il[1] = max(il[1], right)
            else:
                if right <= il[1] and left >= il[0]:
                    # current in the middle of INTERVAL
                    continue
                else:
                    il[0] = min(il[0], i[0])
                    il[1] = max(i[1], i[1])
    result.insert(0, tuple(il))
    result = sorted(result, key=lambda x: x[0])
    return result


re = interval_insert([(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8))
re = interval_insert([(1,2)], (3,4))
print(re)
