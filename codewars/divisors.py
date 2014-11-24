'First Kata question'
def divisors(integer):
    def isPrime(integer):
        for i in range(2, integer):
            if integer % i ==0:
                return False
        return True
    def getfactor(integer):
        res = []
        for i in range(2,integer):
            if integer % i ==0 :
                if i not in res:
                    res.append(i)
        return res
    if isPrime(integer):
        return '{} is prime'.format(integer)

    # not prime
    return getfactor(integer)

import unittest
test = unittest.TestCase()

print(divisors(25))
test.assertTrue(divisors(13) == "13 is prime", msg='it is equal')



"""
Test.assert_equals(divisors(15), [3, 5]);
Test.assert_equals(divisors(12), [2, 3, 4, 6]);
Test.assert_equals(divisors(13), "13 is prime");


"""


# Learn better solutions

def divisors(num):
    l = [a for a in range(2,num) if num%a ==0]
    if len(l) ==0:
        return str(num) + ' is a prime'
    return l

print(divisors(49))