# coding: utf-8


def o(msg=None):
    print(('*' * 30 + str(msg) + '*' * 30).center(80))


def order(sentence):
    import re
    # order("is2 Thi1s T4est 3a")
    words = sentence.split()
    words_cnt = len(words)
    out = [None] * words_cnt
    pat = re.compile(r'\d')
    for idx, i in enumerate(words):
        m = re.search(pat, i)
        if m:
            # print(m.group())
            out[int(m.group()) - 1] = i

    return ' '.join(out)


print(order("is2 This1 T4test 3a"))
