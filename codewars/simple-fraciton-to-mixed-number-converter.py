

from fractions import Fraction
import re


def mixed_fraction(s):
    if s.count('-') > 1:
        s = s.replace('-', '')
    pattern = re.compile(r'(-?\d+)/(-?\d+)$')
    result = re.match(pattern, s)
    if not result:
        return 'not valid s'
    numer, deno = int(result.group(1)), int(result.group(2))

    # zero
    if deno == 0:
        raise ZeroDivision("zero devision error happend!")
    if numer == 0:
        return 0

    # simple
    fractions = Fraction(numer, deno)
    output = ''
    if fractions < 0:
        output += '-'
        fractions *= -1
    numer, deno = fractions.numerator, fractions.denominator
    int_part, new_numer = divmod(numer, deno)


    #print int_part, new_numer, deno, fractions
    fract_part = '{}/{}'.format(new_numer, deno)
    if new_numer == 0: return output + str(int_part)
    if int_part in (0,1):
        return output + fract_part
    return output + str(int_part) + fract_part

for t in ['42/9', '6/3', '4/6', '0/188', '-10/7', '-3988791/5992333', '9309376/-4654688', '-5389358/9955676']:
    print mixed_fraction(t)
