'cool solution'


def palindrome_chain_length(n, count=0):
    if str(n) == str(n)[::-1]: return count
    else: return palindrome_chain_length(n + int(str(n)[::-1]), count+1)



def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    def isPalindrome(n):
        if n < 10 or (n < 100 and n % 11 == 0):
            return True
        return isPalindrome(int(str(n)[1:-1])) if str(n)[0] == str(n)[-1] else False
    def reverse(n):
        return  int(''.join( reversed(str(n)) ))
    step = 0
    while isPalindrome(n) == False:
        step += 1
        n += reverse(n)

    return step

print('palindrome_chain_length')
print(palindrome_chain_length(87))
print('done')

def isPalindrome(n):
    if n < 10 or (n < 100 and n % 11 == 0):
        return True
    return isPalindrome(int(str(n)[1:-1])) if str(n)[0] == str(n)[-1] else False
def reverse(n):
    return  int(''.join( reversed(str(n)) ))
print(isPalindrome(12))
# s = 'abcde'
# print( ''.join(list( reversed(s)) ))
# n = 123
# print(int(''.join( reversed(str(n)) )) )

# # print(int(reverse(str(30))))

# def isPalindrome(n):
#         if n < 10 or (n < 100 and n % 11 == 0):
#             return True
#         return isPalindrome(int(str(n)[1:-1])) if str(n)[0] == str(n)[-1] else False

# print(isPalindrome(123))


# print(isPalindrome(1221))
# print(isPalindrome(121))