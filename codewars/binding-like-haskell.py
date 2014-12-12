def bind(lst,func):
    # Implement meee!
    return [ func(i)[0] for i in lst]

print(bind([1,2,3], lambda a:  [a ] ))
print(bind([1,2,3], lambda a:  [ [a] ] ))
print(bind([1,2,3], lambda a:  [ [a, -a] ] ))
print(bind([1,2,3], lambda a:  [ str(a) ] ))