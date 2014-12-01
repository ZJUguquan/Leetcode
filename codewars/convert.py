def convert(input, source, target):
    """BEGIN"""



'''
test.describe('example tests')
bin = Alphabet.BINARY; oct = Alphabet.OCTAL; dec = Alphabet.DECIMAL; hex = Alphabet.HEXA_DECIMAL;
allow = Alphabet.ALPHA_LOWER; alup = Alphabet.ALPHA_UPPER; alpha = Alphabet.ALPHA; alnum = Alphabet.ALPHA_NUMERIC;

test.it('should convert between numeral systems')
test.assert_equals(convert("15", dec, bin), '1111', '"15" dec -> bin');
test.assert_equals(convert("15", dec, oct), '17', '"15" dec -> oct');
test.assert_equals(convert("1010", bin, dec), '10', '"1010" bin -> dec');
test.assert_equals(convert("1010", bin, hex), 'a', '"1010" bin -> hex');

test.it('should convert between other bases')
test.assert_equals(convert("0", dec, alpha), 'a', '"0" dec -> alpha');
test.assert_equals(convert("27", dec, allow), 'bb', '"27" dec -> alpha_lower');
test.assert_equals(convert("hello", allow, hex), '320048', '"hello" alpha_lower -> hex')
test.assert_equals(convert("SAME", alup, alup), 'SAME', '"SAME" alpha_upper -> alpha_upper');
'''