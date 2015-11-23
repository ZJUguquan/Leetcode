def prime_factors(n):
    if n <= 0:
        n = -n
    f, res = 3, []
    # if is_prime(n):
    #     return [n]
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
    res = set(res)
    return list(res)

print(prime_factors(54))


def factors(x):
    if type(x) != int or x < 1:
        return -1

    if x == 1:
        return [1]

    res = [
        i for i in range(1, int(x**.5 + 1)) if float(float(x) / i) == float(x // i)]
    result = [1, x]
    while res:
        pop = res.pop()
        if pop not in result:
            result.extend([pop, x // pop])
    return sorted(set(result), reverse=True)


print(factors(120))
