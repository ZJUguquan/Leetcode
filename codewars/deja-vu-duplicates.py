# coding: utf-8



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