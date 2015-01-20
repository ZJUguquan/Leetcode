def rgb(*args):
  return "".join(hex(min(255,max(0,x)))[2:].zfill(2).upper() for x in args)

def rgb(r, g, b):
    res = ''
    for i in (r, g, b):
        if i > 255:
            i = 255
        if i < 1:
            i = 0
        temp = hex(i)[2:]
        if len(temp) < 2:
            temp = '0' + temp
        res += temp.upper()

    return res


print(rgb(255, 255, 255))
print(rgb(148, 0, 211))