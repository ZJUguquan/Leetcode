
class Solution:
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0:
            return 0
        counter, j = 0, 0
        while j < n:
            if A[counter] == A[j] :
                j += 1
            else:
                counter +=1
                A[counter] = A[j]
                j +=1
        return (counter+1)

s = Solution()

A = [1,1,2,]
print(s.removeDuplicates(A))



