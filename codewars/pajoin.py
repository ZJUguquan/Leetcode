import os

import os
def mkdirp(*directories):
    """Recursively create all directories as necessary"""
    res = ''.join( directories)
    # res = res.replace('\\','/')
    return os.mkdir(res)

# os.path.join(*directories)


a = mkdirp("/tmp","directories","can","be","made","recursively")
print(a)

# print(mkdir("/tmp","directories","can","be","made","recursively"))
"""
mkdirp("/tmp","directories","can","be","made","recursively")
test.expect(os.path.exists('/tmp/directories/can/be/made/recursively'),
            '/tmp/directories/can/be/made/recursively does not exist')
"""

print(a.replace('/','\\'))