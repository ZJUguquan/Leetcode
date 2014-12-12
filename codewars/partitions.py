

'Other AC'

def partitions(n, k=1, cache={}):
    if k > n: return 0
    if n == k: return 1
    if (n,k) in cache: return cache[n,k]
    return cache.setdefault((n,k), partitions(n, k+1) + partitions(n-k, k))



'虽然可以 但是花的时间太久了.'

def partitions(n):
    '''define a function which returns the number of integer partitions of n'''
    pass


def step(total, first_step):
    'first_step is the max value'
    if first_step < 2 :
        return max(first_step,1)
    if total < 3:
        return total
    if first_step >= total:
        return step(total, total-1) + 1
    return step(total- first_step, first_step) + step(total, first_step-1)

print(step(5, 4))
print(step(25, 25))
# print(partitions(10))



'''
这应该是一个组合数学的问题
Test.expect(partitions(1) == 1)
Test.expect(partitions(5) == 7)
Test.expect(partitions(10) == 42)
Test.expect(partitions(25) == 1958)
'''