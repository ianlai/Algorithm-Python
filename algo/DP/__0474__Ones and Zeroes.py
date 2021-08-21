# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    
    #Top-Down DP + Precalulate matrixZeroOne + Better getMatrixZeroOne [O(len + m*n): 81%]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        print("Top-Down DP + Precalulate matrixZeroOne + Better getMatrixZeroOne")
    
        def dfs(strs, m, n, idx):
            if m < 0 or n < 0:
                return -1
            if idx >= len(strs):
                return 0 
            if (m, n, idx) in self.memo:
                return self.memo[(m, n, idx)]

            countNoUse = dfs(strs, m, n, idx+1)
            countUse   = 1 + dfs(strs, m - self.matrix[idx][0], n - self.matrix[idx][1], idx+1)
            self.memo[(m, n, idx)] = max(countNoUse, countUse)
            return self.memo[(m, n, idx)]

        def getMatrixZeroOne(arr):
            matrixZeroOne = [(s.count("0"), s.count("1")) for s in arr]
            return matrixZeroOne
        
        if not strs:
            return 0
        self.memo = {}
        self.matrix = getMatrixZeroOne(strs)
        return dfs(strs, m, n, 0)
    
    # =============================================================

    #Top-Down DP + Precalulate matrixZeroOne  [O(len + m*n): 81%]
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        print("Top-Down DP + Precalulate matrixZeroOne ")
    
        def dfs(strs, m, n, idx):
            if m < 0 or n < 0:
                return -1
            if idx >= len(strs):
                return 0 
            if (m, n, idx) in self.memo:
                return self.memo[(m, n, idx)]

            countNoUse = dfs(strs, m, n, idx+1)
            countUse   = 1 + dfs(strs, m - self.matrix[0][idx], n - self.matrix[1][idx], idx+1)
            self.memo[(m, n, idx)] = max(countNoUse, countUse)
            return self.memo[(m, n, idx)]

        def getMatrixZeroOne(arr):
            matrixZeroOne = [[0 for _ in range(len(arr))] for _ in range(2)]
            for idx, string in enumerate(arr):
                matrixZeroOne[0][idx] = string.count("0")
                matrixZeroOne[1][idx] = string.count("1")
            return matrixZeroOne
        
        if not strs:
            return 0
        self.memo = {}
        self.matrix = getMatrixZeroOne(strs)
        return dfs(strs, m, n, 0)
    
    # =============================================================
    
    #Top-Down DP [O(m*n*len): 49%]
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        print("Top-Down DP 1")
        if len(strs) == 0:
            return 0
        memo = {}
        return self.dfs1(strs, m, n, 0, memo)
    
    def dfs1(self, strs, m, n, idx, memo):
        if m < 0 or n < 0:  #Should check this first
            return -1
        if idx >= len(strs):
            return 0
        if (m, n, idx) in memo:
            return memo[(m, n, idx)]
        
        zero, one = self.getZeroAndOne1(strs[idx])
        
        countNoUse = self.dfs1(strs, m, n, idx + 1, memo)
        countUse   = 1 + self.dfs1(strs, m-zero, n-one, idx + 1, memo)
        #print(m, n, idx, "->", countNoUse, countUse)
        
        memo[(m, n, idx)] = max(countNoUse, countUse)
        return memo[(m, n, idx)]
    
    def getZeroAndOne1(self, s):
        zero, one = 0, 0
        for c in s:
            if c == "0":
                zero += 1
            if c == "1":
                one += 1
        return zero, one             