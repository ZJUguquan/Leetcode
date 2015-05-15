def fives(n):
    fives = 0
    while n % 5 == 0 and n > 0:
        fives += 1
        n = int(n//5)
    return fives

def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0


print(zeros(100))
