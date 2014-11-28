
'better solution'

def is_monotone(heights):
  for i, item in enumerate(heights):
    if i > 0 and heights[i-1] > item: return False
  return True

def is_monotone(heights):
    '''Determine if heights are monotone'''
    if len(heights) < 2: return True
    for i in range(len(heights)):
        if i <= len(heights)  -2 :
            if heights[i+1] < heights[i]:
                return False
    return True

l = [1,2,3]
print(is_monotone(l))