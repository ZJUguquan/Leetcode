
# other
def Dragon(n):
    if not isinstance(n, int) or n < 0:
        return ''
    s = 'Fa'
    for i in xrange(n):
        s = 'aRbFR'.join(t.replace('b', 'LFaLb') for t in s.split('a'))
    return s.replace('a', '').replace('b', '')


















import re
def multiple_replace(dict, text):

  """ Replace in 'text' all occurences of any key in the given
  dictionary by its corresponding value.  Returns the new tring."""
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

#
# You may combine both the dictionnary and search-and-replace
# into a single object using a 'callable' dictionary wrapper
# which can be directly used as a callback object.
#

# In Python 2.2+ you may extend the 'dictionary' built-in class instead
from UserDict import UserDict
class Xlator(UserDict):

  """ An all-in-one multiple string substitution class """

  def _make_regex(self):

    """ Build a regular expression object based on the keys of
    the current dictionary """

    return re.compile("(%s)" % "|".join(map(re.escape, self.keys())))

  def __call__(self, mo):

    """ This handler will be invoked for each regex match """

    # Count substitutions
    self.count += 1 # Look-up string

    return self[mo.string[mo.start():mo.end()]]

  def xlat(self, text):
    self.count = 0
    return self._make_regex().sub(self, text)




text = "Larry Wall is the creator of Perl"

dict = {
"Larry Wall" : "Guido van Rossum",
"creator" : "Benevolent Dictator for Life",
"Perl" : "Python",
}

#print multiple_replace(dict, text)

def Dragon(n):
    from string import maketrans
    s = 'Fa'
    mapping = {'a': 'aRbFR', 'b': 'LFaLb'}
    i = 0
    while i < n:
        s = multiple_replace(mapping, s)
        i  += 1
    return s.replace('a', '').replace('b', '')

print(Dragon(2))

# FRFRRLFLFR
# FRFRRLFRFRLFR

# from turtle import right, left, forward, speed, exitonclick, hideturtle

# def dragon(level=4, size=200, direction=45):
#     if level:
#         right(direction)
#         dragon(level-1, size/1.41421356237, 45)
#         left(direction * 2)
#         dragon(level-1, size/1.41421356237, -45)
#         right(direction)
#     else:
#         forward(size)

# speed(0)
# hideturtle()
# dragon(6)
# exitonclick() # click to exit