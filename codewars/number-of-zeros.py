def fives(n):
    fives = 0
    while n % 5 == 0 and n > 0:
        fives += 1
        n = int(n//5)
    return fives

def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0
# cache = {}
# def zeros(n):
#     if

#     res = 0
#     five = 5
#     while five <= n:
#         temp = len([i for i in range(5, n+1, five)])
#         res += len(temp)
#         five *= 5
#     if n not in cache:
#         cache[n] = res
#     return res

# print(fives(100))
print(zeros(100))
# print([fives(c) for c in  range(0,111,5) ] )
