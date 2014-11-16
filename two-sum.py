
"TLE"
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) == 2:
            return (1,2)
        for i in range(0, len(num)  -1 ):
            left = num[i]
            if target - num[i] not in num[:i] + num[i+1:]:
                pass
            else:
                return (i + 1, num.index(target - num[i])+ 1 )

s = Solution()
print(s.twoSum([1,2,3,12,5], 14))


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) == 2:
            return (1,2)
        dest = {}
        for i in range(0, len(num)):
        	if (target - num[i]) in dest:
        		ans = (i+1, dest[target-num[i]])
        		if (ans[0] > ans[1]):
        			ans = (ans[1], ans[0])
        		return ans
        	dest.setdefault(num[i], i+1)


s = Solution()
print(s.twoSum([3,2,4], 6))