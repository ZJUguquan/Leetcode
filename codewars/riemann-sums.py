def xxrange(start, stop, step):

    while start < stop:
        yield start
        start += step


def left_riemann(f, n, a, b):
    sum = 0
    step = (b-a) / 10000.0
    for ss in xxrange(a, b, step):
        sum += f(ss) * step
    return  round(sum, 3)

# Part I
def left_riemann(f, n, a, b):
  h = float(b-a)/n
  print(h)
  sum = 0
  x = a
  for i in range(n):
    sum += f(x) * h
    x += h
  return round(sum * 100)/100


# riemann sums II (trapezoidal rule)

def riemann_trapezoidal(f, n, a, b):
  h = float(b-a)/n
  sum = 0
  x = a
  for i in range(n):
    sum += float(f(x) + f(x+h))/2 * h
    x += h
  return round(sum * 100)/100


