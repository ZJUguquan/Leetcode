'Sierpinski Gasket'
'other'

def sierpinski(n):
  if not n:
    return 'L'

  prev = sierpinski(n-1).split('\n')
  return '\n'.join(prev + [l.ljust(len(prev[-1])) + ' ' + l for l in prev])


def sierpinski(n):
    if n == 0:
        return 'L'
    elif n == 1:
        temp = ['L', 'L L']
        return '\n'.join(temp)
    else:
        temp = list(sierpinski(n-1).split('\n'))
        space_temp = [ i +' '* (2**(n)- len(i))+ i for i in temp]
        return  '\n'.join(temp) + '\n' + '\n'.join(space_temp)


print(sierpinski(2))
print('*'*20)
print(sierpinski(3))