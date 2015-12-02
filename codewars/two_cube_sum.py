

def has_two_cube_sums(n):
    if n < 100:
        return False
    mr = int(n ** 0.3334)

    options = {i ** 3: i for i in range(1, mr + 1)}
    solutions = []

    for i in range(1, mr + 1):
        if n - i ** 3 in options:
            if options[n - i ** 3] > 0 and i != options[n - i**3]:
                solutions.append((i, options[n - i**3]))

    if len(solutions) > 3:
        # print mr, solutions
        return True
    return False


print has_two_cube_sums(1729)

print has_two_cube_sums(4104)

print has_two_cube_sums(4105)

# Test.assert_equals(has_two_cube_sums(1), False)
# Test.assert_equals(has_two_cube_sums(1729),True) # 9^3 + 10^3 and 1^3 + 12^3
# Test.assert_equals(has_two_cube_sums(42), False)
# Test.assert_equals(has_two_cube_sums(4104), True)
# Test.assert_equals(has_two_cube_sums(4105), False)
