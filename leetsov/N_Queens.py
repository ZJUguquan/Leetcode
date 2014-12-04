
# from itertools import permutations

# n = 8
# cols = range(n)

# def board(vec):
#     print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n")

# for vec in permutations(cols):
#     if n == len(set(vec[i]+i for i in cols)) \
#          == len(set(vec[i]-i for i in cols)):
#         print ( vec )
#         board(vec)

n, r = 10 , 3
indices = list(range(n))
cycles = list(range(n, n-r, -1))
pool = [i for i in range(1,11)]
a = tuple(pool[i] for i in indices[:r])
print(a)
print(indices, cycles)
def peryjy(n):
    result = []
    if n == 1:
        p = [1]; result.append(p)
        return result
    if n == 2:
        pass

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    # such as n = 10, r = 3,
    indices = list(range(n)) # [0....9]
    cycles = list(range(n, n-r, -1))  #[ 10, 9, 8]
    yield tuple(pool[i] for i in indices[:r])  # 取前3个元素
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return




"***********************************************************"

'Reference from http://en.wikibooks.org/wiki/Algorithm_Implementation/Miscellaneous/N-Queens'
# def queensproblem(rows, columns):
#     solutions = [[]]
#     for row in range(rows):
#         solutions = add_one_queen(row, columns, solutions)
#     return solutions

# def add_one_queen(new_row, columns, prev_solutions):
#     return [solution + [new_column]
#             for solution in prev_solutions
#             for new_column in range(columns)
#             if no_conflict(new_row, new_column, solution)]

# def no_conflict(new_row, new_column, solution):
#     return all(solution[row]       != new_column           and
#                solution[row] + row != new_column + new_row and
#                solution[row] - row != new_column - new_row
#                for row in range(new_row))

# for solution in queensproblem(8, 8):
#     print(solution)



#from itertools import product

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

#print(list( product(list(range(4)), repeat = 4)) )
# print(list(product([1,2,3])  ))

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


# print(list(permutations([1,2,3])))