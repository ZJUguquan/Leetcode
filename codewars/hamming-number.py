# Description:
'time out'

'solution'



# A Hamming number is a positive integer of the form 2i3j5k, for some
# non-negative integers i, j, and k.

# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in example test fixture.

# Your code should be able to compute all of the smallest 5,000 Hamming
# numbers without timing out.


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
        return True

# print([i for i in range(6, 100) if is_prime(i)])
# import pdb; pdb.set_trace()  # breakpoint 5bd6f467 //



def hamming(n):
    factors = [2, 3, 5]
    elements = [1 for i in range(n)]
    nextIndex = [0 for i in range(len(factors)) ]
    nextFrom = factors[::]#[0 for i in range(len(generator)) ]
    for i in range(1, n):
        nextNumber = 2**64
        for j in nextFrom:
            if j < nextNumber:
                nextNumber = j
        elements[i] = nextNumber
        for j in range(len(factors)):
            if nextFrom[j] == nextNumber:
                nextIndex[j] += 1
                nextFrom[j] = elements[nextIndex[j]] * factors[j]
        # print(elements)
    return elements[-1]
    #print(nextNumber)

print(hamming(10))

