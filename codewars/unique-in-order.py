def unique_in_order(iterable):
    rest = []
    for p in iterable:
        if rest == [] or p != rest[-1]:
            rest.append(p)
    return rest


iterable = 'ABBCcAD'

print(unique_in_order(iterable))