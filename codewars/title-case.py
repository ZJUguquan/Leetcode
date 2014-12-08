'better solution'
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])



from string import capwords
def title_case(title, minor_words=''):
    if minor_words == '':
        return capwords(title)
    ignore_words = [w.lower() for w in minor_words.split()]
    res = ''; words= title.split()
    for i in range(len(words)):
        if i == 0:
            res += words[0].capitalize()
            res += ' '
        else:
            w = words[i]
            if w.lower() not in ignore_words:
                res += w.capitalize()
            else:
                res += w.lower()
            res += ' '
    return res.strip()

print(title_case('the  quick bronw fox'))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
# ```
# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# Example:
#     title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
# ```