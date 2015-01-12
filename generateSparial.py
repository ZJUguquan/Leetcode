
def generateSparial(n):
    if n < 0 :
        return None
    if n == 1:
        return [1]
    res = [ [0 for i in range(n)] for j in range(n)]
    levelNum = n //2
    num = 1
    for l in range(levelNum):
        for i in range(l, n-1):
            res[l][i] = num
            num += 1
