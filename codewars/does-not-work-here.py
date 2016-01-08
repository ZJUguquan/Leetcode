def find_employees_role(name):
    if " " not in name:
        return 'Does not work here!'
    firstname, lastname = name.split()[:2]
    print(name)
    for emp in employees:
        if emp["first_name"] == firstname and emp["last_name"] == lastname:
            return emp["role"]
    return 'Does not work here!'
