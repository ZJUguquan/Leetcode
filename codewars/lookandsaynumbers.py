'Much  Much better solution '

from itertools import groupby

def look_and_say(data='1', maxlen=5):
    L = []
    for i in range(maxlen):
        data = "".join(str(len(list(g)))+str(n) for n, g in groupby(data))
        L.append(data)
    return L




def look_and_say(data='1', maxlen=5):
    #TODO populate result list with the look and say numbers
    ''' data:   starting number set
          maxlen: max sequence length
    '''
    def count_and_say(data='1'):
        if data is None:
            return ''
        if len(data) ==1 : return '1'+data
        from collections import OrderedDict
        res = ''
        count = 0
        for idx, dgt in enumerate(data):
            # print(res)
            if idx == 0:
                count = 1
            elif idx <= len(data)-2:
                if dgt == data[idx-1]:
                    count += 1
                else:
                    res += str(count) + data[idx-1]
                    count = 1
            elif idx == len(data) - 1:
                if dgt == data[idx-1]:
                    count += 1
                    res += str(count) +dgt
                    return res
                else:
                    res += str(count) + data[idx-1]
                    res += '1'+dgt
                    return res
    result = []
    last_layer = data
    #result.append(data)
    for layer in range(1, maxlen+1):
        last_layer = count_and_say(last_layer)
        result.append(last_layer)
    return result



# first to consider maxlen = 1
def count_and_say(data='1'):
    if data is None: return ''
    if len(data) ==1 : return '1'+data
    from collections import OrderedDict
    res = ''; count = 0;
    for idx, dgt in enumerate(data):
        # print(res)
        if idx == 0:
            count = 1
        elif idx <= len(data)-2:
            if dgt == data[idx-1]:
                count += 1
            else:
                res += str(count) + data[idx-1]
                count = 1
        elif idx == len(data) - 1:
            if dgt == data[idx-1]:
                count += 1
                res += str(count) +dgt
                return res
            else:
                res += str(count) + data[idx-1]
                res += '1'+dgt
                return res

print(count_and_say('1'))

# from collections import OrderedDict
# d = OrderedDict.fromkeys('abcde')

print(look_and_say('1', 10))

print(look_and_say('132', 8))