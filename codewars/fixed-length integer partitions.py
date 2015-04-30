def indices(n, d):
    if d == 0:
        return [[0] * n]
    if n == 1:
        return [d]
    if n == 2:
        return [[i, d-i] for i in range(0, d+1)]

    res =[]
    if n > 2:
        for i in range(0, d+1):
            # print(i)
            if i >= 0:
                lower_dim = indices(n-1, d-i)
                # print(type(lower_dim))
                for ele in lower_dim:
                    ele.extend([i])
                    if ele not in res and sum(ele) == d:
                        res.append(ele)
            else:
                pass
    return res

# print(indices(2,2))

print(indices(3, 2))


# print([ [] ] * 10 )
