'my puzzle of PYthon'

print( [str(a) + str(b) for a in ["1","2"] for b in ["a", "b"] ] )
# 1a ....

from pinyin import PinYin

test = PinYin()
test.load_word()
a = test.hanzi2pinyin(string='钓鱼岛是中国的')
print(a)

# Python 3 renamed the unicode type to str
unicode_or_str = "钓鱼岛是中国的"

print()