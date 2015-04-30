def namelist(names):
    _len = len(names)
    output = ''
    if _len == 1:
        output = names[0]['name']

    else:
        for idx, pair in enumerate(names):
            name = pair['name']
            if idx < _len - 2:
                output += name+', '
            if idx == _len - 2:
                output += name+' & '
            if  idx == _len - 1:
                output += name
    # print(output)
    return output

names = [ {'name': 'Bart'}, {'name': 'Lisa'} , {'name': 'Maggie'} ]

namelist(names)