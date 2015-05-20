# coding: utf-8
#


def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()


print song_decoder("AWUBBWUBC")
print song_decoder("AWUBWUBWUBBWUBWUBWUBC")
print song_decoder("WUBAWUBBWUBCWUB")