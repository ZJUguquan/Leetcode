def largest(n, xs):
    "Find the n highest elements in a list"

    return sorted(xs)[-n:];


def solution(string, ending):
    return string.endswith(ending)