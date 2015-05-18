
import locale

def group_by_commas(d):
    # locale.setlocale(locale.LC_ALL, 'en_US')
    return "{:,}".format(d)


print(group_by_commas(12132))