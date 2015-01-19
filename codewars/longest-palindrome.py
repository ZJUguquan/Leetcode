
def longest_palindrome(text):
    text = text.lower()
    results = []
    if text == '':
        return 0
    if len(text) == 1 or len(text) == len(set(text)):
        return 1
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1] and chunk not in results:
                results.append(chunk)
    if results == []:
        return 1
    return len(max(results, key=len))


-- ans

def isPalindrome(s):
    return all(s[i] == s[-1 - i] for i in xrange(len(s) // 2))

def longest_palindrome(s):
    if not s:
        return 0
    ret = 1
    for i in xrange(len(s) - 1):
        for j in xrange(len(s), i + 1, -1):
            if isPalindrome(s[i:j]):
                ret = max(ret, j - i)
    return ret