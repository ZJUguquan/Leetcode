'''Cycle Detection: Floyd's The Tortoise and the The Hare'''


def h(x):
    return (x + 1) % 175


def floyd(f, x0):
    tortoise, hare = f(x0), f(f(x0))
    while tortoise != hare:
        hare = f(f(hare))
        tortoise = f(tortoise)
    # find the first position mu of first repetition
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lambda1 = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lambda1 +=1
    return [mu, lambda1]

print(floyd(h, 0))

'''result
simple case: pass
failed:  should handle complex sequences: logistic map
[0, 88] should equal [85, 8]


question descriptor
There is 3 phases for the algorithm:



2) At this point the tortoise position has walked ν, the hare 2ν, the distance between them is both ν and kλ. So hare starting at his last position moving in cycle one step at a time and tortoise at x0 moving towards the cycle will intersect at the beginning of the cycle. This is how to find μ.

3) Now that they are in the same position, tortoise stay still and hare move in the circle one step at a time, lambda is incremented at each step. So when they meet again we will have lambda.

You will build a function that take f and x0 as parameters and return an array [mu, lambda]. All the function will be periodic after some point.

We can find an application of this algorithm for greater purpose, as for exemple Pollard Rho Algorithm for integer factorisation.
'''