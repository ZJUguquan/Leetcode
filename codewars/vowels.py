import collections

vowels = 'aeiou'


def find_solutions(words):
    possible = collections.defaultdict(list)
    for word in words:
        for i, letter in enumerate(word):
            if letter in vowels:
                possible[word[:i] + '.' + word[i + 1:]].append(word)
    solutions = sorted(sorted(x) for x in possible.values() if len(x) == 5)
    return solutions
