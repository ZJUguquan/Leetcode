
def is_vampirenumber(m1, m2):
    if not m1 or not m2:
        return False
    prod = str(m1 * m2)
    str_ = str(m1) + str(m2)
    return sorted(prod) == sorted(str_)
