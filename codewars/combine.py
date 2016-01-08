
# http://www.codewars.com/kata/55e529bf6c6497394a0000b5/train/python
def combine(*args):
    #your code here
    output = []

    length = max([ len( list(x)) for x in args])


    for j in range(length):
    	for ele in args:
            if isinstance(ele, dict):
                ele = [ele]
            else:
                pass
            # ele = list(ele)
            if len(ele) > j:
                output.append(ele[j])

    return output
