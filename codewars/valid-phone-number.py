def validPhoneNumber(phoneNumber):
    import re
    return re.match(r'^\((\d{3})\)\s(\d{3})-(\d{4})$', phoneNumber) is not None

print(
validPhoneNumber("(123) 456-7890"),
validPhoneNumber("(1111)555 2345"),
validPhoneNumber("(098) 123 4567"))


-- other


def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))