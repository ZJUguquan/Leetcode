def maxArea(height):
	j = len(height) - 1
	i, mx = 0, 0
	while (i < j):
		mx = max(mx, ((j-i) *(min(height[i],height[j])) ) )
		if height[i] < height[j]:
			i +=1
		else:
			j -=1
	return mx


"Accept"
	# area = {}
	# for i in range(1, len(height) + 1):
	# 	curr_height = height[i-1]
	# 	max_curr_height = max(height[: i+1])

import random
height = [random.randint(1,20) for i in range(10)]
print(height)
print(maxArea(height) )