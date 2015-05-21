# regex
import re


def increment_string(strng):
    match = re.match(r'(.*?)(\d*)$', strng)
    strs, numbers = match.group(1), match.group(2)
    if not numbers:
        return strs + '1'
    length_numbers = len(numbers)
    return strs + str(int(numbers) + 1).zfill(length_numbers)

print increment_string('str123')
print increment_string('s1231312tr000')
print increment_string('z999')


########################################################################
#
#clever

increment_string=f=lambda s:s and s[-1].isdigit()and(f(s[:-1])+"0",s[:-1]+str(int(s[-1])+1))[s[-1]<"9"]or s+"1"