def compose(f,g):
  return lambda *x: f(g(*x))
"""
add1 = lambda a: a+1
this = lambda a: a

test.expect( compose(add1,this)(0) == 1 )
"""


add1 = lambda a: a + 1
this = lambda a: a

print(dir(add1))
print(compose(add1, this)([10,11]))