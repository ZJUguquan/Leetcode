

# TRY ALL POSSIBLE BREAK-POINTS
# For any keystroke N, we need to loop from N-3 keystrokes
# back to 1 keystroke to find a breakpoint 'b' after which we
# will have Ctrl-A, Ctrl-C and then only Ctrl-V all the way.

def hA(N):
    if N < 7:
        return N
    else:
        maxa = 0
        for b in range(N-3, 0, -1):
            curr = (N-b-1) * hA(b)
            if curr > maxa:
                maxa = curr
        return maxa

for i in range(1, 20):
    print(hA(i))