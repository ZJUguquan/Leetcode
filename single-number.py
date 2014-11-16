class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        counter = {}
        for ele in A:
            if ele not in counter:
                counter[ele] = 1
            else:
                counter[ele] += 1
        return dict(zip(counter.values(), counter.keys()))[1]
