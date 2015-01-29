def number(lines):
    if len(lines) == 0:
        return []
    n = len(lines)
    result = []
    for i in range(n):
        result.append('%s: %s' %(i+1, lines[i]))
    return result