
class Test(object):

    def assert_equals(self, left, right):
        print left
        print left == right if left != right else 'Oh no'

test = Test()

def chstr(lst):
    print  ' -> '.join(map(str, lst))

def imperfect_fib_rabbits(n, b, death=6):
    if n in (0, 1):
        return 1
    if death <= 1:
        return 0
    immatures, matures, deaths = [1, 0], [0, 1], [0, 0]
    month = 1
    while month <= n:
        # chstr(immatures)
        # chstr(matures)
        # chstr(deaths)
        # print '- ' * 30 + str(month)
        # process of death and birth
        babies = b * matures[-1]

        if len(deaths) < death:
            deaths.append(0)
        else:
            deaths.append(immatures[-death])

        adults = immatures[-1] + matures[-1] - deaths[-1]
        immatures.append(babies)
        matures.append(adults)
        month += 1

    return immatures[n] + matures[n]

print imperfect_fib_rabbits(6, 3, 6)

print imperfect_fib_rabbits(8, 3, 4)



# other shorter

def imperfect_fib_rabbits(n, b, l):
    rabbits = [1] + ([0] * (l - 1))
    for i in range(0, n):
        rabbits = [b * sum(rabbits[1:])] + rabbits[:-1]
    return sum(rabbits)