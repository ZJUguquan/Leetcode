'rank vector'
def ranks(a):
    return [sorted(a, reverse=True).index(i)+1 for i in a]
# def ranks(v):
#     res = []
#     from collections import Counter
#     c = Counter(v)
#     rank = {}
#     for idx,k in enumerate(sorted(c.keys(), reverse=True)):
#         if idx == 0:

#         print(k, c[k])
#     # if len(v) == len(set(v)):
#     #     for i in v:
#     #         rank = sorted(v, reverse=True).index(i) + 1
#     #         res.append(rank)
#     #         return res
def ranks(v):
    from collections import Counter
    c = Counter(v)
    vs = sorted(list(set(v)), reverse=True)
    rank = {}; res = {}
    for i in vs:
        rank[vs.index(i) + 1] = i
    bigger_than_me = 0
    # print('rank:',rank)
    for order, value in sorted(rank.items(), key=lambda x: x[0]) :
        # print(rank, value)
        # print(res)
        if order == 1:
            res[value] = 1
        elif order == 2:
            bigger_than_me = c[rank[1]]
            if value not in res:
                res[value] = bigger_than_me + 1
        else:
            bigger_than_me += c[rank[order-1]]
            if value not in res:
                res[value] = bigger_than_me + 1

    # print(res)
    return [res[i] for i in v]


v = [8, 3, 6, 10, 8]
# v = [9, 3, 6, 10]
v = [3,3,3,3,3,5,1]
v = [2, 2]
print(ranks(v))


# def makesortcount(v):
#     if v == []:
#         return {}
#     v_sorted = sorted(v)
#     counter = [v_sorted.count(i) for i in v_sorted]
#     counter_rank = {}
#     for ele in counter:
#         if ele not in counter:
