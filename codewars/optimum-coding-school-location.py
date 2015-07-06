def distance(students, center):
    dis = 0

    for s in students:
        dis += abs(s[0] - center[0]) + abs(s[1] - center[1])
    return dis


def optimum_location(students, locations):
    mini = 999999
    curr_id = -1
    for idx, location in enumerate(locations):
        curr = distance(students, [location['x'], location['y']])
        if curr < mini:
            mini = curr
            curr_id = idx
    info = locations[curr_id]
    return "The best location is number {id} with the coordinates x = {x} and y = {y}".\
                format(id=info['id'], x=info['x'], y=info['y'])
