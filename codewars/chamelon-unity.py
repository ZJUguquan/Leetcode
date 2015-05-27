# coding: utf-8


# chameleons is int[3], desiredColor is int from 0 to 2

def Chameleon(chameleons, desiredColor):
    print chameleons, desiredColor
    color_count = dict(zip(['r', 'g', 'b'], chameleons))
    target = ['r', 'g', 'b'][desiredColor]
    other_color = [i for i in ['r', 'g', 'b'] if i != target]
    to_meet =sorted([(k, color_count[k]) for k in other_color], key=lambda x: x[1])

    if to_meet[0][1] == to_meet[1][1]:
        return to_meet[0][1]
    meets = to_meet[0][1]
    meet_left = to_meet[1][1] - meets
    color_count[target] +=  to_meet[0][1]
    # print meet_left, meets
    if meet_left % 3 != 0 or color_count[target] == 0:

        return -1
    return meets + meet_left

print Chameleon([34, 32, 35], 0)



# others
# chameleons is int[3], desiredColor is int from 0 to 2
def Chameleon(chameleons, desiredColor):
    '''
      Whenever color change happens, number of chameleons of
      each color changes in (-1, -1, +2) pattern, or, by modulo 3,
      (-1, -1, -1). Thus, if numbers of chameleons of other two
      colors have different residues of division by 3, that will
      never change - but in the end, we need them both be 0.
    '''
    def SolutionExists(cham, color):
        if cham[color]==0 and (cham[(color+1)%3]==0 or cham[(color+2)%3]==0):
            return False
        return ((cham[(color+1)%3]%3) == (cham[(color+2)%3]%3))
    '''
      Say, our target color is red, and there are more blue
      chameleons than green ones. If we have only red and blue
      chameleons, sequence (B+R->GG, B+G->RR, B+G->RR) effectively
      converts three blue chameleons into red ones in three steps.
      And if we have both blue and green, we can use (B+G->RR).
      This way, we need a number of steps equal to the number of
      blue chameleons. Because there is no way to change color of
      two blue chameleons in one step, this method is fastest.
    '''
    def ShortestSolution(cham, color):
        return max(cham[(color+1)%3], cham[(color+2)%3])

    if not SolutionExists(chameleons, desiredColor): return -1
    return ShortestSolution(chameleons, desiredColor)