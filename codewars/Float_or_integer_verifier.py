def i_or_f(arr):
    try:
        if type(float(arr)) == float :
            return True
    except:
        return False



print('1E1'.lower().count('e'))
print(i_or_f('1e+1'))
print(i_or_f(0))

print(i_or_f('1ee1'))