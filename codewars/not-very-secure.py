


def alphanumeric(text=''):
    import string
    valid_letters = string.ascii_letters + string.digits
    if len(text) < 1: return False

    for i in text:
        if i not in valid_letters:
            return False
    return True

print(
alphanumeric('heelo')
)
