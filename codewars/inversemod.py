def inverseMod(a, m):
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None


# print(inverseMod(2,5))
# print(inverseMod(48,101))
# print(inverseMod(2, 40))



from unittest import TestCase
test =TestCase()

test.assertEqual(inverseMod(2,5), 3)
test.assertEqual(inverseMod(48,99999997), 40)
