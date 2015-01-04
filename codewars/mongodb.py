from datetime import datetime

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        if not isinstance(s, str): return False
        if len(s) == 24:
            return all(c in '0123456789abcdef' for c in s)
        return False

    @classmethod
    def get_timestamp(cls, s):
        if not cls.is_valid(s):
            return False
        return datetime.fromtimestamp(int(s[:8], 16))