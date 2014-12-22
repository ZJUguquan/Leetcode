def service(score):
    f, s = map(int, score.split(':'))
    return 'first' if (f + s) % 2 == 0 else 'second'

print(service('3:2'))

