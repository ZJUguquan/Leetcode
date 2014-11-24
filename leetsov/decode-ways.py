class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        length=len(s)
        if length==0:
            return 0
        D=[0]*(length+1)
        D[-1]=1
        D[-2]=1 if int(s[-1])>=1 and int(s[-1])<=26 else 0
        for i in range(length-2,-1,-1):
            bridge=True if int(s[i:i+2])>=10 and int(s[i:i+2])<=26 else False
            bonus=D[i+2] if bridge==True else 0
            if int(s[i])!=0:
                D[i]=D[i+1]+bonus
            else:
                D[i]=0

        return D[0]
# class Solution {
# public:
#     int numDecodings(string s) {
#         if (s.empty()) return 0;
#         int t1=s.back()=='0'?0:1, t2=1, rv=t1;
#         for (int i=s.size()-2; i>=0; i--) {
#             if (s[i]=='0') rv=0;
#             else rv=t1+(atoi(s.substr(i, 2).c_str())<=26?t2:0);
#             t2=t1;
#             t1=rv;
#         }
#         return rv;
#     }
# };

def numDecodings(s):
    if s is None:
        return 1
    letter2num = dict(zip([chr(x) for x in range(ord('A'), ord('Z')+1 )], [str(x) for x in range(1,27) ]  ))
    num2letter = dict(zip(letter2num.values(), letter2num.keys()))

    if '00' in s or s =='':
        return 0
    if s[0] == '0':
        return 0
    if '0' in s:
        first_zero = s.index('0')
        zeronumber = int(s[first_zero-1:first_zero+1])
        # print(zeronumber)
        first_part = s[:first_zero-1]
        second_part = s[first_zero+1:]
        if zeronumber == 10 or zeronumber == 20 :
            return numDecodings(first_part) * numDecodings(second_part)
        else:
            return 0
    num = int(s)
    if len(s) == 1:
        if num > 0 and num < 10:
            return 1
    buffernumber = int(s[:2])
    if buffernumber == 10 or buffernumber == 20 :
        return numDecodings(s[2:])
    elif buffernumber % 10 == 0:
        return 0
    elif buffernumber > 26:
        return 2* numDecodings(s[2:])
    elif buffernumber <=26:
        return 3 * numDecodings(s[2:])
    # for i in range(len(s)):
    #     bufferzone = ''
    #     if i <= len(s) - 2: # i+1 valid
    #         bufferzone = s[i] + s[i+1]
    #         buffernumber = int(bufferzone)
    #         if buffernumber==10 or buffernumber ==20:
    #             return numDecodings(s[:i]) * numDecodings(s[i+2:])
    #         elif buffernumber % 10 == 0 :
    #             return 0
    #         elif buffernumber >= 27:
    #             return numDecodings(s[:i]) *2* numDecodings(s[i+2:])
    #         else:
    #             return numDecodings(s[:i]) *3* numDecodings(s[i+2:])


s = '120203'
# print(s.index('0'))
print(numDecodings(s))


letter2num = dict(zip([chr(x) for x in range(ord('A'), ord('Z')+1 )], [str(x) for x in range(1,27) ]  ))
num2letter = dict(zip(letter2num.values(), letter2num.keys()))
# print(letter2num)
# print(num2letter)