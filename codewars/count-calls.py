def add(a, b):
  return a + b


def add_ten(a):
  return add(a, 10)


def misc_fun():
  return add(add_ten(3), add_ten(9))

def count_calls(func, *args, **kwargs):
  """Count calls in function func"""

  rv = func(*args, **kwargs)

  return calls, rv



def alphabet_position(text):
    import string
    return ' '.join([ str(ord(i.lower()) - ord('a') + 1) for i in text if i in string.ascii_letters])

print(alphabet_position('yangjinyong jin yong '))

def bind(lst,func):
    # Implement meee!
    return [ func(i)[0] for i in lst]

print(bind([1,2,3], lambda a:  [a ] ))
print(bind([1,2,3], lambda a:  [ [a] ] ))
print(bind([1,2,3], lambda a:  [ [a, -a] ] ))
print(bind([1,2,3], lambda a:  [ str(a) ] ))
