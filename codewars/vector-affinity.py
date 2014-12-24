def vector_affinity(a, b):
    long = max(len(a), len(b)) * 1.0
    short = min(len(a), len(b))
    return sum([1 for i in range(short) if a[i] == b[i]])/long


a = [1,2,3]
a = [6]
b = [1,2,3,4,5]
b = [6,6,6,6,6,6]
print(vector_affinity(a,b))