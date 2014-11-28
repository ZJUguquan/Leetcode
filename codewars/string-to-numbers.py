def string_to_number(s):
    # ... your code here
    return int(s) if s[0] != '-' else -1 * int(s[1:])