def solution(number):
    A, B, C = 0, 0, 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 !=0:
            A+=1
        elif i %5 == 0 and i % 3!=0:
            B+=1
        elif i % 15 == 0:
            C+=1
    return [A,B,C]


'better solution'

def solution(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15
    return [A - C, B - C, C]

print(solution(300))
'''
Write a function that takes an integer and returns an Array [A, B, C] where A is the number of multiples of 3 (but not 5) less than the given integer, B is the number of multiples of 5 (but not 3) less than the given integer and C is the number of multiples of 3 and 5 less than the given integer.

For example, solution(20) should return [5, 2, 1]
'''