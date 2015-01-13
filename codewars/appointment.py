
'check solution 查看答案后 解'


def time2int(time):
    '''a string time format transmit to a int(miniutes)'''
    hour, min = time.split(':')
    return int(hour) * 60 + int(min)


def get_start_time(schedules, duration):
    # flatten and sort
    merged_schedules = [
        meeting for schedule in schedules for meeting in schedule]
    merged_schedules.sort(key=lambda meeting: meeting[0])
    open_start = '09:00'
    open_stop = '09:00'

    for meeting in merged_schedules:
        if meeting[0] > open_stop:
            open_stop = meeting[0]
        if time2int(open_stop) - time2int(open_start) >= duration:
            return open_start
        if meeting[1] > open_start:
            open_start = meeting[1]
    open_stop = '19:00'
    if time2int(open_stop) - time2int(open_start) >= duration:
        return open_start
    return None


'finding an appointment'
schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'],
     ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]


def timetoint(interval):
    s, e = interval
    s_f = float(s.split(':')[0]) + float(s.split(':')[1]) / 60
    e_f = float(e.split(':')[0]) + float(e.split(':')[1]) / 60
    return [s_f, e_f]

# print(timetoint(['11:30', '12:15']))


# def isInsect(i1, i2):
#     a, b = i1
#     c, d = i2
#     if (a >= c and a < d) or (c >= a and c < b):
#         return True
#     return False


# def union(i1, i2):
#     a, b = i1
#     c, d = i2
#     if isInsect(i1, i2):
#         return [min(a, c), max(b, d)]

# import itertools


# def get_start_time(schedules, duration):
#     duration /= 60
#     raw_start, raw_end = 9, 19
#     all_slices = list(itertools.chain(*schedules))
#     all_slices = [timetoint(i) for i in all_slices]
#     all_slices = sorted(all_slices, key=lambda x: x[0])
#     zero = [9, 9]
#     un_state = []
#     un_state.append(zero)
#     for t_slice in (all_slices):
#         for z in un_state:
#             if isInsect(z, t_slice):
#                 un_state.pop(un_state.index(z))
#                 z = union(z, t_slice)
#                 un_state.append(z)
#             else:
#                 un_state.append(t_slice)
#     return zero, un_state

#     # else:

print(get_start_time(schedules, 60))
