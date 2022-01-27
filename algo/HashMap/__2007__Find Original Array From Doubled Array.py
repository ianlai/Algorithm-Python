from typing import List
import collections
import unittest
class Solution:
    
    # Count Map + Sorting [O(n + klogk): 54%]  (數字數:n ; 不同數個數:k)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        print("Code2")
        original = []
        changedCount = collections.defaultdict(int)
        for v in changed:
            changedCount[v] += 1            
        for v in sorted(changedCount.keys()):
            if changedCount[v] == 0:
                continue
            if changedCount[v * 2] == 0:
                return []
            else:
                if v == 0:
                    count = changedCount[v]
                    if count % 2 != 0:
                        return []
                    original.extend([v] * (count // 2))
                else:
                    count = changedCount[v]
                    changedCount[v] -= count
                    changedCount[v * 2] -= count
                    original.extend([v] * count)
        return original

class UnitTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Solution().findOriginalArray([]), [])

    def test_invalid_changed1(self):
        self.assertEqual(Solution().findOriginalArray([2,4,3,1]), [])
    
    def test_invalid_changed2(self):
        self.assertEqual(Solution().findOriginalArray([0,16,8,2,0,0,4,16,0,8,8]), [])

    def test_valid_changed1(self):
        self.assertEqual(Solution().findOriginalArray([4,2,1,2]), [1,2])

    def test_valid_changed2(self):
        self.assertEqual(Solution().findOriginalArray([0,16,8,2,0,0,4,16,0,8,4,8]), [0,0,2,4,8,8])


if __name__ == "__main__":
    unittest.main()
    #print(Solution().findOriginalArray([2,4,3,1]))
    #print(Solution().findOriginalArray([2,4,2,1]))

    # ============================================================
        
    # Array [TLE]
    def findOriginalArray1(self, changed: List[int]) -> List[int]:
        print("Code1")
        original = []
        changedSet = changed
        for v in changedSet:
            #v = changedSet.pop()
            #changedSet.append(v)
            #print(v, changedSet)
            if v % 2 != 0: #odd
                if v * 2 in changedSet:
                    original.append(v)
                    changedSet.remove(v)
                    changedSet.remove(v * 2)
                else:
                    return []
        changedSet.sort(reverse=True)
        #print(changedSet)
        while changedSet:
            v = changedSet.pop()
            #changedSet.remove(v)
            #print(v)
            if v * 2 in changedSet:
                original.append(v)
                changedSet.remove(v * 2)
            else:
                if v // 2 in changedSet:
                    original.append(v // 2)
                    changedSet.remove(v // 2)
                else:
                    return []
            #print(changedSet)
        return original