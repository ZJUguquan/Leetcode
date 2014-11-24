#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

i1 = Interval(1,3)
i2 = Interval(2,6)
i3 = Interval(8,10)
i4 = Interval(15,18)
"""
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals[0]
        intervals = sorted(intervals, key=lambda x:x.start)

        j = 0
        for i in intervals[1:]:
            if i.start <= intervals[j].end:
                if i.end > intervals[j].end:
                    intervals[j].end = i.end
                else:
                    intervals[j].end = intervals[j].end
            else: # i.start right at j.end
                j += 1
                intervals[j].start = i.start
                intervals[j].end = i.end
            # print( [(k.start, k.end) for k in intervals])
            # print(j)

        for k in range(1, len(intervals)-j):
            intervals.pop()
        return intervals



s = Solution()
intervals= [i1,i2,i3,i4]
result = s.merge(intervals)
for i in result:
    print(i.start, i.end)


print([] == None) # False


# print( ([] is None]) )