# '''
# Instructions
# Output
# Regex Failure - Bug Fixing #2

# Oh no, Timmy's received some hate mail recently but he knows better. Help timmy fix his regex filter so he can be awesome again!

# '''

import re
from re import sub


def filter_words(phrase):
    return sub(r'[(bad)|(mean)|(ugly)|(horrible)|(hideous)]', "awesome", phrase, re.IGNORECASE)


# print filter_words("You're Bad! timmy!")  # ,"You're awesome! timmy!")

print filter_words("You're MEAN! timmy!")  # ,"You're awesome! timmy!")
