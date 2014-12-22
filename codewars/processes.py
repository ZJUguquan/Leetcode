'solution'
def processes(start, end, processes):
    queue = [([], start)]
    while queue:
        path, dest = queue.pop()
        if dest == end:
            return path
        queue.extend((path + [p[0]], p[2]) for p in processes if p[1] == dest)
    return []

# In this task you have to code process planner.

# You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of [process_name, start_thing, end_thing]). You must return names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

# If start already equals end, return [], since no path is required.

# Example:
''


# processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
# processes('field', 'ferrari', test_processes) # should return []
# processes('field', 'field', test_processes) # should return [], since no processes are needed
from pprint import pprint
class process(object):
    def __init__(self, start_thing, process_name):
        self.start_thing = start_thing
        self.process_name = process_name

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
]
def processes(start, end, processes):

    res = []
    next_work = {}
    i_need_do = {}
    for i in processes:
        next_work[i[1]] = i[2]
        i_need_do[i[1]] = i[0]
    # print(next_work)
    # print('*'*20)
    # print(i_need_do)
    if start == end or start not in next_work or end not in next_work.values():
        return []
    now_i_have = start
    while now_i_have != end:
        #print('now i have', now_i_have)
        if now_i_have not in next_work:
            res = []
            break
        res.append(i_need_do[now_i_have])
        now_i_have = next_work[now_i_have]
        if now_i_have == start:
            res = []
            return res
        #print('now_i_have', res, 'do')
    return res
# print(processes('filed', 'field', test_processes))
# print(processes('field', 'ferrari', test_processes))
print(processes('field', 'bread', test_processes))