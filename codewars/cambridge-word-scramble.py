def change(word):
    from random import shuffle

    if len(word) <= 3:
        return word
    else:
        idx = range(1, len(word)-1)
        shuffle(idx)
        return word[0] + ''.join([word[i] for i in idx]) + word[-1]


def mix_words(s):
    output = ""
    import string
    word = ''
    for idx, ele in enumerate(s):

        if ele not in string.ascii_letters:
            output += change(word) + ele
            word = ''
        else:
            word += ele
    if word:
        output += change(word)

    return output



print(mix_words("yang jin yong hohohhaha!!!"))
from random import shuffle

a= [1,2,3,4,5]
shuffle(a)

print(a)

# Testing if mix_words really shuffle
# This is a random test with extremely remote chance for a false negative; retry if you think your function really works randomly: 'JdepMbLnNQhAGmcuqxPYsZfagrTvwilKEkOyHBRIXWStVUFjCzDo' should not equal 'JdepMbLnNQhAGmcuqxPYsZfagrTvwilKEkOyHBRIXWStVUFjCzDo'
