# coding: utf-8


def format_duration(seconds):
    if not seconds: return 'now'
    times = [(86400*365, 'years'),  (86400, 'days'), (3600, 'hours'), (60, 'minutes'), (1, 'seconds')]
    res = []
    for unit, name in times:
        qutient, seconds = divmod(seconds, unit)
        if not qutient:
            continue
        else:
            res.append(str(qutient) + ' ' + (name if qutient > 1 else name[:-1]))

    if len(res) == 1:
        return res[0]
    elif len(res) == 2:
        return ' and '.join(res)
    else:
        output_string = ''
        for idx, ele in enumerate(res):
            if idx < len(res) - 2:
                output_string += ele + ', '
            elif idx == len(res) - 2:
                output_string += ele + ' and '
            else:
                output_string += ele
        return output_string

########################################################################
# test
print format_duration(1)
print format_duration(62)
print format_duration(120)
print format_duration(3600)
print format_duration(3662)
print format_duration(123)

# # test not pass
# '4 year, 68 days, 3 hours and 4 minutes' should equal
# '4 years, 68 days, 3 hours and 4 minutes'

# year should be years (definition error!!!)