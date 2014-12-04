# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# __author__ = 'STEVE'
# __tag__ = "LeetCode"
# __status__ == "Accepted"


s = [1,2,3,4]
result = []
for m in s:
	q = s
	q.remove(m)
	result.append(q)

print result


'能实现 效率可能有点低'
def subset(S):
	A = [[]]
	S.sort()
	for n in S:
		for i in range(len(A)):
			ss = A[i][:]
			ss.append(n)
			A.append(ss)
	return A

print subset([1,2])

"效率更好的方法"

def subset(S):
	R = [[]]
	for s in sorted(S):
		R += [ r + [s] for r in R]
	return R
print subset([1,2,3])


"+ 对于列表 相当于连接运算 "
print [1] + [2]






# 	re = [ ]
# 	S.sort()
# 	i = 1
# 	for i in range(0,len(S)):
# 		n = len(re)
# 		for j in (range(0, n)):
# 			re.append(re[j])
# 			re.append(S[i])
# 	return re
# print subset([1,2,3])