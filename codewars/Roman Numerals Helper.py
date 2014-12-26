"Roman Numerals Helper"


class RomanNumerals(object):
    @classmethod
    def to_roman(cls, num):
        m = {1000: "M",
             900: "CM",
             500: "D",
             400: "CD",
             100: "C",
             90: "XC",
             50: "L",
             40: "XL",
             10: "X",
             9: "IX",
             5: "V",
             4: "IV",
             1: "I"}
        if num in m.keys():
            return m[num]
        for i in sorted(m.keys(), reverse=True):
            if num >= i:
                return m[i] + RomanNumerals.to_roman(num - i)
        return ""

    @classmethod
    def from_roman(cls, s):
        m = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        s = s.upper()
        stack = [0]
        # reversed
        for c in s[::-1]:
            if m[c] >= stack[-1]:
                stack.append(m[c])
            else:
                v = stack.pop()
                stack.append(v - m[c])
        return sum(stack)

print(
RomanNumerals.to_roman(4), # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
)