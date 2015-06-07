


purpose = '''Write a function that will take a list of coin denominations and a desired amount and provide the least amount of coins needed.'''




def loose_change(cva, n, output=None):
    if output is None:
        output= n
    if len(cva) < 1:
        return None
    if n in cva:
        return 1
    if min(cva) > n:
        return 0
    cva = sorted(cva, reverse=True)
    for idx, each in enumerate(cva):
        if each > n:
            continue
        if n - each in cva:
            return 2
        use_it = loose_change(cva, n-each)
        if use_it is not None:
            if use_it < output:
                output = use_it
        not_use_it = loose_change(cva[idx+1:], n)
        if not_use_it is not None:
            if not_use_it < output:
                output = not_use_it




print loose_change([1,5,10, 25], 37)