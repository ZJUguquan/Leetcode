def last(*args):
    arg = args[0]
    if len(args) == 1 and (hasattr(arg, "__iter__") or type(arg) == type('s')):
        return arg[-1]
    return args[-1]
    # if len(args)> 1:
    #     return list(args)[-1]
    # else:
    #     arg = args[0]
    #     if type
    #     return list(arg)[-1]


print(last([1,2,3]))
print(last('abc'))
print(last(300))
print(last(3,4,5))