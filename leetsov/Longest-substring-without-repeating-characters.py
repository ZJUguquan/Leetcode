'Longest-substring-without-repeating-characters'

def lengthOfLongestSubstring(s):
	if len(s)<=1:
		return len(s)
	maxlen = 0
	templen = 0
	charused = {}
	start = 0
	for i in range(len(s)):
		if s[i] not in charused or charused[s[i]] < start:
			charused[s[i]] = i
			templen += 1
			maxlen = max(maxlen, templen)
		elif s[i] in charused:
			start = charused[s[i]] + 1
			charused[s[i]] = i
			templen = i - start + 1
			maxlen = max(maxlen, templen)
	return maxlen

s = "abcabcbb"
s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
a = lengthOfLongestSubstring(s)
print(a)