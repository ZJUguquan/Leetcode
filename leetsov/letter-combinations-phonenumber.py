'letter-combinations-phonenumber'

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letterdict = {"1":[""], "2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k",'l'],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"],"0":[" "]}
	def product(l1, l2):
		res = []
		for e1 in l1:
			for e2 in l2:
				res.append(e1+e2)
		return res
	if len(digits) == 0:
		return [""]
	elif len(digits) == 1:
		return letterdict[digits]
	elif len(digits) == 2:
		return product(letterdict[digits[0]], letterdict[digits[1]])
	else:
		top2 = self.letterCombinations(digits[:2])
		return product(top2, self.letterCombinations(digits[2:]))
teststring = '234'
rest = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(letterCombinations(teststring))