
def compare_versions(v1,v2):
    if v1 == v2:
        return True
    v1s = list(map(int, v1.split('.')))

    v2s = list(map(int, v2.split('.')))


    for i in range(min(len(v1s), len(v2s))):
        print(i)
        if v1s[i] != v2s[i]:
            return v1s[i] >= v2s[i]

        else:
            continue
    return False




v1 = '10.4.1'
v2 = '10.4'
print(compare_versions(v1,v2))


# clever edtion


def compare_versions(version1, version2):
    split_version = lambda version: map(int, version.split('.'))
    return split_version(version1) >= split_version(version2)
