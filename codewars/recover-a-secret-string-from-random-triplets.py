'solution others'

def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res


# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. ['w', 'h', 'i'] is a triplet for the string 'whatisup'.

# As a simplification, you may assume that no letter occurs more than once in the secret string.

# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.


# secret = "whatisup"

triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
    ]


def pool(triplets):
    secret = []
    sorted_triplets = sorted(triplets)
    row = len(triplets)
    first_letters_option = set([b[0] for b in sorted_triplets if len(b) >=1])
    second_letter_option = set([b[1] for b in sorted_triplets if len(b)>=2])
    third_letter_option =  set([b[2] for b in sorted_triplets if len(b) >= 3])
    if len(first_letters_option) == 0:
        return []
    # print(first_letters_option)
    # print((second_letter_option.union(third_letter_option)) )
    first_letter = first_letters_option - (second_letter_option.union(third_letter_option))
    temp = first_letter.pop()
    secret.append(temp)
    first_letters_option.discard(temp)
    for i in triplets:
        if len(i) > 0:
            if i[0] ==  secret[-1]:
                # print(i)
                i.remove(i[0])
    return secret + pool(triplets)

def recoverSecret(triplets):
    res = pool(triplets)
    return ''.join(res)

print(recoverSecret(triplets))



    # return
# test.assert_equals(recoverSecret(triplets), secret)

'''
print(first_letters_option, second_letter_option, third_letter_option, end='\n')
    # find the 1st letter
    for e in set(first_letters_option):
        if e not in (second_letter_option + third_letter_option) :
            secret.append(e)

    first_letters_option = [i for i in first_letters_option if i != secret[-1]]
    while len(first_letters_option)>0 or :
        for e in set(first_letters_option):
            if e not in (second_letter_option + third_letter_option) :
                secret.append(e)
        first_letters_option = [i for i in first_letters_option if i != secret[-1]]
    print(secret, first_letters_option)
'''

lis = ['w','h','s']
for i in lis:
    if i == 'w':
        lis.remove(i)
# print(lis)