'TextJustify'
'AC'
def fullJustify(self, words, L):
    l = len(words)
    if l == 0:
        return []
    if L == 0:
        return [""]
    result = []
    i = 0
    tmpLine = words[0]
    if l == 1:
        result.append(self.oneline(tmpLine,L))
        return result
    else:
        i = 0
        while i < l:
            if i == l-1:
                extraSpace = L - len(tmpLine)
                tmpLine += " "*extraSpace
                result.append(tmpLine)
                return result
            tmpLine2 = tmpLine + ' ' + words[i+1]
            if len(tmpLine2) > L:
                result.append(self.oneline(tmpLine,L))
                tmpLine = words[i+1]
            else:
                tmpLine = tmpLine2
            i += 1


def oneline(self,line,L):
    line_split = line.split()
    if line_split == []:
        return ' '*L
    line_nospace = line.replace(' ','')
    numOfSpace = L - len(line_nospace)
    numOfGap = len(line_split) - 1
    if numOfGap == 0:
        result = line_nospace+" "*numOfSpace
        return result
    else:
        evenSpace,extraSpace = divmod(numOfSpace,numOfGap)
        i = 0
        result = ""
        while i < numOfGap:
            result += line_split[i]
            if extraSpace != 0:
                result += " "*(evenSpace+1)
                extraSpace -= 1
            else:
                result += " "*(evenSpace)
            i += 1
        result += line_split[-1]
        return result