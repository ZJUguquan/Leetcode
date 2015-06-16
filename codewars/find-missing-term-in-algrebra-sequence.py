

def find_missing(sequence):
    print sequence
    n = len(sequence)
    s = sum(sequence)
    fl = sequence[0] + sequence[-1]
    if n % 2 == 0 and fl//2 not in sequence:
        return fl// 2

    have_been_as = (fl) * n //2
    if  s == have_been_as :
        return 2*sequence[0] - sequence[1]

    return  (fl) * (n+1) //2- s


lst = range(1, 11, 2)
lst.pop(3)

lst = [1,3,5,9]
lst = [1, 2, 3, 4, 6, 7, 8, 9]
print find_missing(lst)