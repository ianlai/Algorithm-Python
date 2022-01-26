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