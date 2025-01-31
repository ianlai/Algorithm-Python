from collections import defaultdict
from math import inf 
import unittest

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


amap = defaultdict(int)
amap[3] = 333
for k, v in amap.items():
    print(k, v)

def findMax(arr) -> int:
    if arr is None:
        return None
    largest = -inf 
    for v in arr:
        largest = max(largest, v)
    return int(largest)

print(findMax([3,7,5,2]))


class UT(unittest.TestCase):
    def test1(self):
        self.assertEqual(findMax([3,5,4,9,1]), 9)
    def test2(self):
        self.assertEqual(findMax([0]), 0)
    def test3(self):
        self.assertEqual(findMax([-8,-3,-1]), -1)
    def test4(self):
        self.assertEqual(findMax(None), None)
unittest.main()