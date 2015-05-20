
# oneline

def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])



def gimme(ia):
    mi, ma = min(ia), max(ia)
    if mi == ma:
        return 0
    for idx, ele in enumerate(ia):
        if mi < ele < ma:
            return idx
