def prefill(n,v=''):
    try:
        n = int(n)
        return [v] * n
    except Exception as e:
        raise TypeError('%s is invalid' % n)

