

def SJF(jobs, index):
    start = 0

    target = jobs[index]

    left_duplicates = jobs[:index].count(target)

    for idx, ele in enumerate(sorted(jobs)):
        if ele == target:
            return start + target * (left_duplicates+1)
        else:
            start += ele

print SJF([3, 10, 20, 1, 2], 0)

print (SJF([100], 0), 100)
print (SJF([3, 10, 20, 1, 2], 0), 6)
print (SJF([3, 10, 20, 10, 2], 3), 25)
