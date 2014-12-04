def spread(func, args):
    return func(*args)



print(spread(lambda x,y,z: z*(x+y), [1,2,3]))