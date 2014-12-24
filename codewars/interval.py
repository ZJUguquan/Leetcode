def interval_insert(myl, interval):
    # outer
    _left, _right = interval
    if _left == _right:
        return myl
    if _left > myl[-1][-1] or _right < myl[0][0]:
        return myl + [interval]
    if _left == myl[-1][-1]:
        return myl[:-1] + [(myl[-1][0], _right)]
    if _right == myl[0][0]:
        return [(_left, myl[0][1])] + myl[1:]

    # crossed
    left_bond = _left
    for each_interval in myl:


def overlaps((a_start, a_end), (b_start, b_end)):
    return (a_start <= b_start and a_end >= b_start) or
        (a_end >= b_start and a_end <= b_end) or
        (b_start <= a_start and b_end >= a_start) or
        (b_end >= a_start and b_end <= a_end)

def union((a_start, a_end), (b_start, b_end)):
    return min(a_start, b_start), max(a_end, b_end)

def interval_insert(myl, interval):
    myl = list(myl)
    target = None
    i = 0
    while i < len(myl):
        if target is not None and overlaps(myl[i], myl[target]):
            myl[target] = union(myl[i], myl[target])
            myl.pop(i)
        elif target is None and overlaps(myl[i], interval):
            target = i
            myl[i] = union(myl[i], interval)
            i += 1
        else:
            i += 1
    if target is None:
        myl.append(interval)
    return myl

from unittest import TestCase
test = TestCase()
test.assertEquals(interval_insert([(1,2)], (3,4)), [(1, 2), (3, 4)])
test.assertEquals(interval_insert([(3,4)], (1,2)), [(1, 2), (3, 4)])

# test.assertEquals(interval_insert([(1,2), (3, 4)], (2,3)), [(1, 4)])
# test.assertEquals(interval_insert([(1,2), (3, 4), (5, 6)], (2,3)), [(1, 4), (5, 6)])
