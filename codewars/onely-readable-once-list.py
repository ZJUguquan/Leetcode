'read once list'


class SecureList(list):
    def __getitem__(self, key):
        ret = list(self)[key]
        del self[key]
        return ret

    def __repr__(self):
        ret = list(self).__repr__()
        del self[:]
        return ret

    def __str__(self):
        ret = list(self).__str__()
        del self[:]
        return ret
