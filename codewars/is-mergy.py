
# http://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
def is_merge(s, part1, part2):
    print s
    print part1
    print part2

    if part1 == '':
        return s == part2
    if part2 == '':
        return s == part1
    if s == '':
        return part1 == part2 == ''

    char = s[0]
    if char not in (part1[0], part2[0]):
        return False
    elif char == part1[0]:
        return is_merge(s[1:], part1[1:], part2)
    else:
        return is_merge(s[1:], part1, part2[1:])


# print is_merge('codewars', 'code', 'wars')
# print is_merge('codewars', 'cdw', 'oears')
# print not is_merge('codewars', 'cod', 'wars')

# print is_merge('wars', 'w', 'ars')
# print is_merge('ewars', 'w', 'ears')

def is_merge(s, part1, part2):
    # print s
    # print part1
    # print part2

    if part1 == '':
        return s == part2
    if part2 == '':
        return s == part1
    if s == '':
        return part1 == part2 == ''

    char = s[-1]
    if char not in (part1[-1], part2[-1]):
        return False
    elif char == part1[-1]:
        print '>>>', (s[:-1], part1[:-1], part2)
        return is_merge(s[:-1], part1[:-1], part2)
    else:
        print '>>>', (s[:-1], part1, part2[:-1])
        return is_merge(s[:-1], part1, part2[:-1])
a = 'Can we merge it? Yes, we can!'
b = 'nw mege eea'
c = 'Ca er it?Ys, w cn!'

print is_merge(a, b, c)