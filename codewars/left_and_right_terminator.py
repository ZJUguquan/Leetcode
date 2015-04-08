
def left(string,i=1):
    if isinstance(i, int):
        # print('int')
        if i == 0:
            return ''
        if i >= len(string):
            return string
        if i < 0:
            return string.split(' ')[0]
        else:
            return string[:i]
    else:
        return string.split(i)[0]


def right(string,i=1):
    if isinstance(i, int):
        if i == 0:
            return ''
        if i >= len(string):
            return string
        if i < 0:
            return string.split()[-1]
        else:
            return string[-i:]
    else:
        return string.split(i)[-1]

text = 'Hello (not so) cruel World!'

# print("***********************************************************")
# left(text,5)   # -> 'Hello'
# print("***********************************************************")

# left(text,-22) # -> 'Hello'
# left(text,1)   # -> 'H'
# left(text)     # -> 'H' too
# left(text,0)   # -> ''
# left(text,99)  # -> 'Hello (not so) cruel World!'
right(text,6)  # -> 'World!'
right(text)    # -> '!'

#== with string as 2nd argument ==
left(text,'o') # -> 'Hell'
right(text,'o')# -> 'rld!'
left(text,' ') # -> 'Hello'  // -- string may be a space