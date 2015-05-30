

import re
# channel challenge 6
url = 'http://www.pythonchallenge.com/pc/def/channel.html'
# url = url[:-12] + 'zip.html'
from urllib import urlopen
# print urlopen(url).read().find('zip')


import zipfile

zip_file = zipfile.ZipFile("channel.zip", "r")


output = []
newname = '90052.txt'
while True:
    start_file = "./channel/{}".format(newname)
    # print dir(zip_file)
    # print zip_file.infolist()
    subfile = zip_file.getinfo(newname)
    # print dir(subfile)
    output.append(subfile.comment)

    try:
        content = open(start_file, 'r').read()
        newname = re.search(r'nothing is (\d+)', content)
        newname = newname.group(1) + '.txt'
    except:
        break

print ''.join(output)

# for name in file.namelist():
#     # if '46145' in name:
#     data = file.read(name)
#     print name, len(data), repr(data[:20])

# with open('./channel/readme.txt', 'r') as f:
#     print f.read()


# while True:

#     try:
#         f = open('./channel/{}.txt'.format(newname), 'r')
#         contet = f.read()
#         print content
#         newname =  re.search(r'nothing is (\d+)', content).group(1)

#     except Exception:
#         break