
candidates = [2, 3, 5, 6, 7]
target = 7


from ..thinkcspy import thinkcspy01

class Solution:

    def combinationSum(self, candidates, target):
        candidates.sort()
        return self._combinationSum(candidates, target, [])

    def _combinationSum(self, candidates, target, item):
        if not candidates:
            return []

        c = candidates[0]
        if c > target:
            return []
        if c == target:
            return [item + [c]]

        return self._combinationSum(candidates[1:], target, item) + self._combinationSum(candidates, target - c, item + [c])


s = Solution()


# print s.combinationSum(candidates, target)
