def to_camel_case(text):
    import re
    return ''.join([(idx<1 and [word] or [word.title()])[0] for idx, word in enumerate(re.split(r'[-_]', text))] )
text = 'the_stealth_warrior'
print(to_camel_case(text))