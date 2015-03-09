class PrimeFactorizer:
    prime = 0

    def __init__(self, prime):
        self.prime = prime
        self.factor = {}
        factor_list  = self.factorize(prime)
        while len(factor_list) > 0:
            first = factor_list.pop(0)
            if first not in self.factor:
                self.factor[first] = 1
            else:
                self.factor[first] += 1


    def factorize(self, n):
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


    #     return result



print(PrimeFactorizer(240).factor)
print(PrimeFactorizer(13).factor)
