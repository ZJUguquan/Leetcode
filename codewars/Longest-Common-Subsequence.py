def lcs(x, y):
    res = ''
    if x == '' or y == '':
        return ''
    # first property
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        first_choice = lcs(x, y[:-1])
        second_choice = lcs(x[:-1], y)
        if len(first_choice) >= len(second_choice):
        # len(first_choice) == len(second_choice):
        #     return [first_choice, second_choice]
        # elif
            return first_choice
        else:
            return second_choice

    # return set(x) & set(y)


print(lcs('abcdef', 'abc'))
print(lcs('abcdef', 'acf'))
print(lcs('132535365', '123456789'))




import itertools
def lcs(x, y):
  for length in reversed(range(len(x)+1)):
      for xItem in list(itertools.combinations(x, length)):
          for yItem in list(itertools.combinations(y,length)):
              if xItem == yItem:
                  return "".join(xItem)