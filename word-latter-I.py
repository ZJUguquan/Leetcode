'word-ladder'

class Solution:
	def ladderLength(self, start, end, dict):
		if start == end:
			return 1
		all_chars = map(chr, range(ord('a'), ord('z')+1))
		visited = set()
		bfs = [start, None]
		# at which distance the following to be processed
		distance = 2
		while len(bfs)>1:
			word = bfs.pop(0)
			if word is None:
				distance += 1
				bfs.append(None)
				continue

			for i in range(len(word)):
				for char in all_chars:
					new_word = word[:i]+ char+word[(i+1):]
					if new_word == end:
						return distance

					if new_word in dict and new_word not in visited:
						bfs.append(new_word)
						visited.add(new_word)

		return 0

start = 'hit'
end = 'cog'
dict = ['hot','dot','dog','lot','log']
all_chars = map(chr, range(ord('a'), ord('z')+1))
s = Solution()
print(s.ladderLength(start, end, dict))

# def onetransform(word, end, dict):
# 	if word in dict:
# 		diff = 0
# 		for i in range(len(word)):
# 			if word[i] != end[i]:
# 				diff +=1
# 		if diff == 1:
# 			return True
# 	return False

# def getonediffword(start, dict):
# 	diff = 0; result = []
# 	for word in dict:
# 		for i in range(len(start)):
# 			if start[i] != word[i]:
# 				diff +=1
# 		if diff == 1:
# 			result.append(word)

# 	return result
# #print(getonediffword(start, dict))
# # print(onetransform('log','cog',dict))

# def ladderLength(start,end,dict):
# 	if len(getonediffword(start,dict)) > 0:
# 		for nextword in getonediffword(start, dict):
# 			dict.remove(nextword)
# 			return ladderLength(nextword, end, dict)
# 		return True
# 	else:
# 		return False

# #print(ladderLength(start, end, dict))
