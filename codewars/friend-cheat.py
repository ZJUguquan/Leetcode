

def removNb(n):
    result = []
    for i in range(1, n+1):
        if ((1+n)*n - 2*i) % (2*i+2) == 0 :
            j = ((1+n)*n - 2*i) // (2*i+2)
            if j <= n and i !=j :
                result.append((i,j))
    return result


print(removNb(26))