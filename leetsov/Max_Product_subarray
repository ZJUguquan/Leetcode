
class Solution:
    def maxProduct(self,A):
        b, f = 1, 1; n = len(A)
        res = -1<<32
        for i in range(len(A)):
            b *= A[i]
            f *= A[n-i-1]
            res = max(res, max(b, f))
            if b == 0: b = 1
            if f == 0: f = 1
        return res
# print(-1<<32)
s = Solution()
print(s.maxProduct([0]))

"****************************************************************************"


"First try, i think too much???"

# class Solution:
#     # @param A, a list of integers
#     # @return an integer
#     def sign(self,x):
#         if x > 0 :
#             return 1
#         elif x == 0:
#             return 0
#         else:
#             return -1

#     def maxProduct(self, A):
#         n = len(A)
#         if n == 1:
#             return A[0]
#         if n == 2:
#             return max(max(A), A[0]*A[1])

#     # def maxProduct(self, A):
#     #     # A contain at least one number
#     #     if len(A) == 1:
#     #         return A[0]
#     #     n = len(A)
#     #     min_v = min(A)
#     #     max_v = max(A)
#     #     if min_v > 0 or (max_v < 0 and n % 2 == 0):
#     #         result = 1
#     #         for i in A:
#     #             resutl *= i
#     #         return result
#     #     elif max_v <0 and n % 2 == 1:
#     #         return self.maxProduct(A[1:], A[:-1])
#     #     # now have to consider most complicate situcation + -
#     #     if n == 2:
#     #         return max(max(A), A[0]*A[1])
#     #     # n >= 3, min_value <= 0 , max_value > 0

#     #     signment = [self.sign(x) for x in A]
#     #     sum_signment = sum(signment)

#         # positive = []
#         # if A[0] > 0:
#         #     positive.append(A[0])
#         # for i in range(1,len(A)) :
#         #     pass


# A = [2,3,-2,4,6,7,-2,-3]
# #s = [1,1,-1,1,1,1,-1,-1]