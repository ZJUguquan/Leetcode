def delete_nth(order,max_e):
    from collections import defaultdict
    d = defaultdict(int)
    r = []
    for i in order:
        if d[i] < max_e:
            d[i] += 1
            r.append(i)
        else:
            continue
    return r

print delete_nth([1,1,3,3,7,2,2,2,2], 3)