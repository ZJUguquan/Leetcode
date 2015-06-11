
def make_readable(seconds):
    return "%s:%s:%s" % tuple(map(lambda x: str(x).zfill(2), (seconds / 3600, seconds / 60 % 60, seconds % 60)))


def make_readable(seconds):
    hh, mm, ss = 0, 0, 0
    if seconds:
        hh, seconds = divmod(seconds, 3600)
    if seconds:
        mm, ss = divmod(seconds, 60)
    hh = '%02d' % hh
    mm = '%02d' % mm
    ss = '%02d' % ss
    return '{}:{}:{}'.format(hh, mm, ss)


print make_readable(359999)
print make_readable(86399)
print make_readable(0)