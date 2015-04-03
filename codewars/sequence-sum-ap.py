def sum_of_n(n):
    if n == 0: return [0]
    if n > 0:
         return [ i *(i +1) // 2  for i in range(0, n+1)]
    else:
        return [ -i *(i+1) // 2  for i in range(-1, n-2, -1)]
    # d = (n > 0 and [1] or [-1])[0]
    # return [ i *(i +1) * d // 2  for i in range(0, n+1, d)]


print(sum_of_n(-4))