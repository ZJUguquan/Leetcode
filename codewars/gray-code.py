'best solution ever'

def bin2gray(bits):
    return [x^y for x,y in zip(bits,[0]+bits)]
def gray2bin(bits):
    return [reduce(lambda x,y:x^y,bits[:i+1]) for i, _ in enumerate(bits)]



'Raw solution, take long long time.'
from collections import deque

def genegray(nbits):
    from collections import deque
    if nbits == 1:
        return [[0], [1]]
    if nbits == 2:
        return [[0,0], [0,1],[1,1], [1,0]]
    res = []
    # prefix old entries with 0
    for e in genegray(nbits - 1):
        f = deque(e); f.appendleft(0);
        # print(f)
        res.append(f)
    # prefix new entries with 1
    for e in genegray(nbits - 1)[::-1]:
        f = deque(e); f.appendleft(1);
        # res.append(list( deque(e[::-1]).appendleft(1) ))
        # f.appendleft(1)
        res.append(f)

    return [ list(m) for m in res]


def bin2gray(bits):
    n = len(bits)
    if n == 1:
        return bits
    # bits to int  index
    thisint = int(''.join([str(e) for e in bits]), base=2)
    return genegray(n)[thisint]


def gray2bin(bits):
    n = len(bits)
    if  n == 1:
        return bits
    thisint = genegray(n).index(bits)
    return [int(e) for e in  str(bin(thisint))[2:] ]



print('test ')
print(bin2gray([1,0,1]))

print(bin2gray([1,0]))


# print(int('101', base=2),)
print(gray2bin([1,1,1]))

"""
0 0  0
1  01  01
2  10  11

3  011
reference from geeksforgeeks
http://www.geeksforgeeks.org/given-a-number-n-generate-bit-patterns-from-0-to-2n-1-so-that-successive-patterns-differ-by-one-bit/

n-bit Gray Codes can be generated from list of (n-1)-bit Gray codes using following steps.
1) Let the list of (n-1)-bit Gray codes be L1. Create another list L2 which is reverse of L1.
2) Modify the list L1 by prefixing a ‘0  ’ in all codes of L1.
3) Modify the list L2 by prefixing a ‘1’  in all codes of L2.
4) Concatenate L1 and L2. The concatenated list is required list of n-bit Gray codes.

For example, following are steps for generating the 3-bit Gray code list from the list of 2-bit Gray code list.
L1 = {00, 01, 11, 10} (List of 2-bit Gray Codes)
L2 = {10, 11, 01, 00} (Reverse of L1)
Prefix all entries of L1 with ‘0’, L1 becomes {000, 001, 011, 010}
Prefix all entries of L2 with ‘1’, L2 becomes {110, 111, 101, 100}
Concatenate L1 and L2, we get {000, 001, 011, 010, 110, 111, 101, 100}


===================
    Gray code is a form of binary encoding where transitions between consecutive numbers differ by only one bit. This is a useful encoding for reducing hardware data hazards with values that change rapidly and/or connect to slower hardware as inputs. It is also useful for generating inputs for Karnaugh maps.

    Here is an exemple of what the code look like:
    0:    0000
    1:    0001
    2:    0011
    3:    0010
    4:    0110
    5:    0111
    6:    0101
    7:    0100
    8:    1100
    The goal of this kata is to build two function bin2gray and gray2bin wich will convert natural binary to Gray Code and vice-versa. We will use the "binary reflected Gray code". The input and output will be arrays of 0 and 1, MSB at index 0.

    There are "simple" formula to implement these functions. It is a very interesting exercise to find them by yourself. Otherwise you can look here: http://mathworld.wolfram.com/GrayCode.html for formula and more informations.


    All input will be correct binary arrays.


    Test.describe("bin2gray:")

    Test.it("should return gray code in an array")
    Test.assert_equals(bin2gray([1,0,1]), [1, 1, 1])
    Test.assert_equals(bin2gray([1,1]), [1, 0])

    Test.describe("gray2bin:")

    Test.it("should return binary code in an array")
    Test.assert_equals(gray2bin([1,0]), [ 1, 1])
    Test.assert_equals(gray2bin([1,1,1]), [1, 0, 1])


"""