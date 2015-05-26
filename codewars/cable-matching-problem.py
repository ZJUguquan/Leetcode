
# # Timeout solution.
# def len2(iter):
#     if iter is None or type(iter) == int:
#         return 0
#     return len(iter)

# def cableCalculator_(need, cables):
#     if need < 1 or len(cables) == 0 or need > sum(cables):
#         return 'No result'
#     cables = sorted([i for i in cables if i <= need])
#     output = None
#     if cables[-1] == need:
#         output = [cables.pop()]
#     for i in cables:
#         if need - i in cables:
#             output = [i, need - i]

#     while cables:
#         temp = []
#         temp.append(cables.pop(-1))
#         try:
#             if isinstance(cableCalculator_(need - temp[0], cables), list):
#                 _this = temp + cableCalculator_(need - temp[0], cables)
#                 if output is None or len(_this) > len2(output):
#                     output = _this
#             else:
#                 continue
#         except Exception, e:
#             print str(e)
#             print output, temp,
#             pass

#     if len(output) == 0:
#         return "No result"
#     else:
#         maxi, posix = output[0], 0
#         for idx, each in enumerate(output):
#             if len(each) > maxi:
#                 maxi = len(each)
#                 posix = idx
#         res = sorted(output[posix], reverse=True)
#         return res
#     return 'No result'


# def cableCalculator(need, cables):
#     result = cableCalculator_(need, cables)
#     if result == 'No result':
#         return result
#     return ','.join(map(str, result))




# # def cableCalculator_(need, cables):
# #     output = {}
# #     cables = sorted([i for i in cables if i < cables])
# #     length = len(cables)
# #     if need in cables:
# #         output[1] = [need]
# #     for i in range(1, length+1):
# #         if sum(cables[-i:]) < need:

# #     for i in cables[:length//2+1]:
# #         if need - i in cables:
# #             output[2] = [need - i, i]




def cableCalculator(need, cables, output=None):
    from itertools import combinations as combi
    from collections import defaultdict

    t = cables
    lens = len(t)
    t = [i for i in t if i <= need]
    i = 1
    if output is None:
        output = dict()
    while i < lens:
        pools = list(combi(t, i))
        for each in pools:
            output[sum(each)] = sorted(each, reverse=True)
        i += 1
    if need in output:
        return ','.join(map(str, list(output[need]) ) )
    else:
        return 'No result'

print cableCalculator(200, [10, 10, 23, 4, 5, 67, 889, 150, 50])
print cableCalculator(83, [10, 10, 23, 4, 5, 67, 889, 150, 50])
print cableCalculator(12, [10, 10, 23, 4, 5, 67, 889, 150, 50])



########################################################################


# others fengex


def recursiveSearch(need, cables):
    for cable in cables:
        if cable == need:
            return str(cable)
        if cable < need:
            ret = recursiveSearch(need - cable, cables[1:])
            if ret:
                return '%d,%s' % (cable, ret)

def cableCalculator(need, cables):
    cables.sort(reverse = True)
    if cables and need >= cables[-1] and need <= sum(cables):
        ret = recursiveSearch(need, cables)
        if ret:
            return ret
    return "No result"