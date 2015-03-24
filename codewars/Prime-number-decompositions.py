
def getAllPrimeFactors(n):
    if isinstance(n, int) == False or n < 1:
        return []
    if n == 1:
        return [1]
    f, res = 3, []
    while n % 2 == 0:
        res.append(2)
        n //= 2

    while f * f <= n:
        while n % f == 0:
            res.append(f)
            n //= f
        f += 2
    if n > 1:
        res.append(n)
    res.sort()
    return res

def getUniquePrimeFactorsWithCount(n):
    if isinstance(n, int) == False or n < 1:
        return [[], []]
    if n == 1:
        return [[1], [1]]
    result = getAllPrimeFactors(n)
    final_result = [[], []]
    for element in result:
        if element not in final_result[0]:
            final_result[0].append(element)
            final_result[1].append(1)
        else:
            final_result[1][-1] = final_result[1][-1] + 1
    return final_result

def getUniquePrimeFactorsWithProducts(n):
    if isinstance(n, int) == False or n < 1:
        return []
    if n == 1:
        return [1]
    result = getUniquePrimeFactorsWithCount(n)
    final_result = []
    for idx, ele in enumerate(result[0]):
        final_result.append(ele ** result[1][idx])
    return final_result


n = 2
print(getAllPrimeFactors(n))
print(getUniquePrimeFactorsWithCount(n))
print(getUniquePrimeFactorsWithProducts(n))