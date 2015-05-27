from string import maketrans
class Cipher(object):
    def __init__(self, map1, map2):

        self.maps_encode = maketrans(map1, map2)
        self.maps_decode = maketrans(map2, map1)

    def encode(self, strng):
        return strng.translate(self.maps_encode)

    def decode(self, strng):
        return strng.translate(self.maps_decode)


map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);

print cipher.encode("abc") # => "eta"
print cipher.encode("xyz") # => "qxz"
print cipher.encode("aeiou") # => "eirfg"
print
print cipher.decode("eta") # => "abc"
print cipher.decode("qxz") # => "xyz"
print cipher.decode("eirfg") # => "aeiou"print