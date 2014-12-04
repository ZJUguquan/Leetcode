"Accept!!!! by my own.... "
"5 submits at list"
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if L== 0  or len(words) < 1:
            return [""]
        if L == 1:
            return words
        result = []
        buffer_list = []
        buffer_len = 0

        for i in range(0, len(words)):
            if len(" ".join(buffer_list  ) ) + len(words[i]) +1 > L:
                result.append(self.putwords(buffer_list, L))
                buffer_list = [];
                buffer_len = 0
            buffer_list.append(words[i])
            buffer_len += len(words[i])
            #print("append words",buffer_list, sep='::')

        last_line = " ".join(buffer_list) + " "* (L - len(" ".join(buffer_list) ))
        result.append(last_line)
        if result[0] == "":
            result.pop(0)
        return result

    def putwords(self, words, L):
        total_len = len(''.join(words))
        result = ''
        if total_len == L:
            return ''.join(words)
        space_num = L - total_len
        gaps_num = len(words) - 1
        if gaps_num == 0:
            # just one word
            return ''.join(words) +' '*(space_num)
        else: # more than one gaps  distribute space_num
            m, n = divmod(space_num, gaps_num)
            # top n gaps get m+1 spaces
            # other  get m spaces
            if n == 0:
                return (' '*m).join(words)
            for i in range(n):
                result = result + words[i] + ' '*(m+1)
            for i in range(n, len(words) -1 ):
                result = result + words[i] + ' '*m
            result += words[-1]
            return result


'11-13-2014 Submit Wrong:'




a = ["This", "is", "an", "example", "of", "text", "justification."]
L = 12
# print(putwords(["shall","be"] ,L))
words = ["What","must","be","shall","be."]
words, L = ["Listen","to","many,","speak","to","a","few."], 6

" Test Input"
#["Here","is","an","example","of","text","justification."], 14
s = Solution()

print(s.fullJustify(words,L))
