class Solution:
    
    #Top-Down DP [O(m*n*len): 49%]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        memo = {}
        return self.dfs(strs, m, n, 0, memo)
    
    def dfs(self, strs, m, n, idx, memo):
        if m < 0 or n < 0:  #Should check this first
            return -1
        if idx >= len(strs):
            return 0
        if (m, n, idx) in memo:
            return memo[(m, n, idx)]
        
        zero, one = self.getZeroAndOne(strs[idx])
        
        countNoUse = self.dfs(strs, m, n, idx + 1, memo)
        countUse   = 1 + self.dfs(strs, m-zero, n-one, idx + 1, memo)
        #print(m, n, idx, "->", countNoUse, countUse)
        
        memo[(m, n, idx)] = max(countNoUse, countUse)
        return memo[(m, n, idx)]
    
    def getZeroAndOne(self, s):
        zero, one = 0, 0
        for c in s:
            if c == "0":
                zero += 1
            if c == "1":
                one += 1
        return zero, one             