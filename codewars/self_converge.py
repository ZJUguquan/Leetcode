def cal_reminder(number):
        descending_number = int(''.join(sorted(str(number), reverse=True)))
        ascending_number = int(''.join(sorted(str(number), reverse=False)))
        reminder = descending_number - ascending_number
        return reminder


def self_converge(number):
    counter = 0
    sub_result = []
    while cal_reminder(number) > 0:
        if cal_reminder(number) in sub_result:
            return counter
        sub_result.append(cal_reminder(number))
        counter += 1
        number = cal_reminder(number)
    return -1


print(
self_converge(123)
)

-- 出题人自己给出的solution

def self_converge (number, kc = None, max_digits = None):
    #print "***init with: ", number, kc, flag

    s_number = str(number)
    len_n = len(s_number)

    # decide whether the number needs padding
    if not max_digits:
        max_digits = len_n  #  set this only during the first call
        kc = [number]
    elif (len_n == max_digits-1):
        s_number = "0" + s_number;

    # form the two numbers to get the difference
    ss_number = "".join(sorted([d for d in s_number]))
    asc       = int (ss_number)
    dsc       = int (ss_number[::-1])
    res       = dsc - asc

    print     dsc, "-", asc, "= ", res, "/   "

    # decide whether to make a recurisve call or not
    if res == 0:
        return -1
    elif len(str(res)) == len(str(number)) and res in kc:
        return 0
    else:
        kc.append(res)
    return 1 + self_converge(res, kc, max_digits)