def new_avg(arr, newavg):
    if not arr: return newavg
    print(arr, newavg)
    print(newavg * float(len(arr)),  sum(arr))
    ex = round(newavg * (len(arr) + 1) - sum(arr))
    if ex > 0 :
        if (ex + sum(arr) ) / float(len(arr)+1) < newavg:
            return ex + 1
        return ex
    else:
        raise ValueError("Error expected")
