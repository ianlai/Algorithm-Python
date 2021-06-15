class Solution:
    
    # Backtracking [O(n^n), 57%]
    # split out 1 char by 1 char (not separate to two substrings)
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        
        strSet = set([])
        return self._maxUniqueSplit(s, strSet, 0)
    
    def _maxUniqueSplit(self, s, strSet, level):
        if not s:
            return 0
        
        maxNumber = 0
        for i in range(1, len(s) + 1):
            ###Debug (layer)
            #for _ in range(level):
            #    print("  ", end = "")
            
            left, right = s[:i], s[i:]
            
            ### Filter in next, not in current
            if left in strSet:
                continue
            
            strSet.add(left)
            #print(left, right, strSet)
            curNumber = 1 + self._maxUniqueSplit(right, strSet, level + 1)
            maxNumber = max(curNumber, maxNumber)
            strSet.remove(left)
            
        return maxNumber
        