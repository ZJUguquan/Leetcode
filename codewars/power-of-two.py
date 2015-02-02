# power of two

def power_of_two(x):
    
    if x in (1,2):
        return True
    while x%2 == 0 and x>0:
        x= x/2
    return True if x == 1 else False

test = [4096, 1024, 1, 2,0, 5, 333 ]
print([power_of_two(i) for i in test])