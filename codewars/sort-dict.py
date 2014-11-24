def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)

testd = {3:1,2:2,1:3}
# for k,v in testd.items():
# 	print(k,v)
print(list(zip(testd.values(), testd.keys())))
from unittest import TestCase
Test = TestCase()
print(sort_dict(sort_dict(testd)))
Test.assertTrue(sort_dict(testd) == [(1,3),(2,2),(3,1)])