class Solution:
    
    # 2022/03/29 
    # Backtracking [O(N*2^N): 52 / O(N): 6%]
    def maxUniqueSplit(self, s: str) -> int:
        print("Code2")
        self.charSet = set()
        def helper(s):
            if not s:
                return 0
            maxCount = 0
            for i in range(len(s)):
                left, right = s[:i+1], s[i+1:]
                if left in self.charSet:
                    continue
                self.charSet.add(left)
                maxCount = max(maxCount, 1 + helper(right))
                self.charSet.remove(left)
            return maxCount
        return helper(s)
            
    # ========================================= 
    # 2021/06/16 
    # Backtracking [57%]
    # split out 1 char by 1 char (not separate to two substrings)
    def maxUniqueSplit1(self, s: str) -> int:
        print("Code1")
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
        