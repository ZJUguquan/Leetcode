def inverseMod(a, m):
    '''
    test.assert_equals(inverseMod(2,5), 3)
    test.assert_equals(inverseMod(48,101), 40)
    '''
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None


print(inverseMod(2,5))
print(inverseMod(48,101))
print(inverseMod(2, 40))