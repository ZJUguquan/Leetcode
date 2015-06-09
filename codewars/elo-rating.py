
def elo(experience, opponent, score, k = None):

    if len(experience) < 1:
        r1 = 1000
    else:
        r1 = experience[-1]

    if k is None:
        if len(experience) >= 30:
            if max(experience) < 2400:
                kk = 15
            else:
                kk = 10
        else:
            kk = 25
    else:
        kk = k(experience)

    print experience, opponent, score, kk

    delta = (opponent - r1) / 400.0
    ea = 1 / (1 + 10 ** delta)

    newscore = r1 + kk * (score - ea)
    return int(round(newscore, 0))