# coding: utf-8

# others


def find_duplicates(e):
    res=[]
    toberemoved=[]
    for i in range(len(e)):
        if i in toberemoved:
            continue

    for j in range(i+1,len(e)):
        if (e[j].first_name==e[i].first_name and e[j].last_name==e[i].last_name and e[j].user_name==e[i].user_name):
            res += [e[j]]
            toberemoved += [j]

    for i in sorted(toberemoved,reverse=True):
        e.pop(i)
    return res


--------------------------------------------------------------------------------

def find_duplicates(employees):
    build_key = lambda e: (e.first_name, e.last_name, e.user_name)

    # Add an attribute for uniqueness comparison
    for e in employees:
        e.dupe_key = build_key(e)

    # Identify duplicates and remove them
    result = []
    first = 0

    while first < len(employees):
        e = employees[first]
        positions = [i for i, emp in enumerate(employees) if e.dupe_key == emp.dupe_key]
        if len(positions) > 1:
            duplicate_positions = positions[1:]
            result.extend([employees[i] for i in duplicate_positions])
            for i in reversed(duplicate_positions):
                del employees[i]
        first += 1

    # Clean up the extra attribute
    for e in employees + result:
        del e.dupe_key

    # Return the dupliactes
    return result










































'''description of problem

It might be déjà vu, or it might be a duplicate day. You’re well trained in the arts of cleaning up duplicates. Someone has hacked your database and

injected all kinds of duplicate records into your tables.

You don’t have access to modify the data in the tables or restore the tables to a previous time because the DBA’s are gone.

You are provided with an array of employees from the server. Your task is to write the findDuplicates function to remove the duplicate records after they are sent down to the client.

Employee Class:

'''

from collections import Counter
def find_duplicates(employees):
    newe = []
    output = []
    for idx, ew in enumerate(employees):
        print ew
        e = Counter([ ew.last_name , ew.user_name , ew.first_name])
        print e
        if e not in newe:
            newe.append(e)
        else:
            output.append(ew)
            del employees[idx]
    print '*' * 80
    print employees
    return output


class Employee:
  def __init__(self,f_name,l_name,u_name):
    self.first_name = f_name
    self.last_name = l_name
    self.user_name = u_name

e = Employee('a','bb','ccc')
print dir(e)
print