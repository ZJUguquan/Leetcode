def filter_used(i):
    if i.endswith('_'):
        return False
    return True

def search_names(logins):
    return [i for i in logins if not filter_used(i[0])]

a = [ [ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]

print(search_names(a))