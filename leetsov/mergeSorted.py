class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        startIndex=0
        for num in B:
            if m == 0:
                A.insert(m,num)
                m=m+1
                continue
            for i in range(startIndex,m):
                if num<A[i]:
                    A.insert(i,num)
                    m=m+1
                    startIndex=i
                    break
                elif i==m-1:
                    A.insert(m,num)
                    m=m+1
                    startIndex=i
                    break