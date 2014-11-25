def hamming(a,b):
  # Implement me!
    return None if len(a) != len(b) else \
        sum([1 for i in range(len(a)) if a[i] != b[i] ])

print(hamming("i love you", "i like you"))


'more beautiful solution'

def hamming(a,b):
  return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))