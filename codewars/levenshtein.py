
'wiki definition'
# It may used, but takes too long time!
# def levenshtein(a,b):
#     i = len(a)
#     j = len(b)
#     if min(i, j) == 0:
#         return max(i, j)
#     # test if last characters of the strings match
#     cost = 1 if a[-1] != b[-1] else 0
#     return min(levenshtein(a[:-1], b) + 1,levenshtein(a, b[:-1]) + 1,
#                levenshtein(a[:-1], b[:-1]) + cost)



'Iterative with full matrix'

def levenshtein_list(str_list_a, str_list_b):
    # for all i and j, d[i,j] will hold the Levenshtein distance between the first i of s and the fist j ## str_list_a has m,  b has n characters
    # note that d has (m+1)*(n+1)
    m = len(str_list_a); n = len(str_list_b); N = max(m,n)
    d = [ [0 for i in range(N+1)] for j in range(N+1)]
    for i in range(1, m+1):
        d[i][0] = i
    for j in range(1, n+1):
        d[0][j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if str_list_a[i-1] == str_list_b[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1,d[i][j-1] + 1,d[i-1][j-1] + 1)
    return d[m][n]

def levenshtein(a,b):
    return levenshtein_list(list(a), list(b))

# str_list_a = list('kitten')
# str_list_b = list('sitting')
# print(levenshtein(str_list_b, str_list_a))


print(levenshtein("sitting", "kitten"))

