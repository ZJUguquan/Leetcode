def find_secret_message(paragraph):
    s = set()
    ret = []
    for w in (word.strip('.,:!?').lower() for word in paragraph.split()):
        if w in s and not w in ret:
            ret.append(w)
        else:
            s.add(w)
    return ' '.join(ret)



-- mine

def find_secret_message(paragraph):
    res = []
    l = [w.lower() for w in paragraph.replace('.','').split()]
    for idx, w in enumerate(l):
        if w in l[idx+1:] and w not in res:
            res.append(w)

    return ' '.join(res)