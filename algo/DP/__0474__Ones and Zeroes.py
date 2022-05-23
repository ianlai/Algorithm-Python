# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    
      # Buttom-Up DP [TLE]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        print("Code6")
        dp = [[[0] * len(strs) for _ in range(n+1)] for _ in range(m+1)]
        
        for k in range(len(strs)):
            count0 = strs[k].count("0")
            count1 = strs[k].count("1")
            for i in range(m+1):
                for j in range(n+1):
                    if k == 0:
                        if i >= count0 and j >= count1:
                            dp[i][j][k] = 1
                    if k > 0:
                        dp[i][j][k] = dp[i][j][k-1]
                        if i >= count0 and j >= count1:
                            dp[i][j][k] = max(dp[i][j][k], 1 + dp[i-count0][j-count1][k-1])
        # for row in dp:
        #     print(row)
        return dp[-1][-1][-1]
    
    
    # Buttom-Up DP [TLE]
    def findMaxForm5(self, strs: List[str], m: int, n: int) -> int:
        print("Code5")
        dp = [[[0] * len(strs) for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                for k in range(len(strs)):
                    count0 = strs[k].count("0")
                    count1 = strs[k].count("1")
                    if k == 0:
                        if i >= count0 and j >= count1:
                            dp[i][j][k] = 1
                    if k > 0:
                        dp[i][j][k] = dp[i][j][k-1]
                        if i >= count0 and j >= count1:
                            dp[i][j][k] = max(dp[i][j][k], 1 + dp[i-count0][j-count1][k-1])
        # for row in dp:
        #     print(row)
        return dp[-1][-1][-1]
    
    
    # 2022/05/23 
    # Memoization DP 
    # T.C. => O(M*N*S): 13%
    # S.C. => O(M*N*S): 23%
    def findMaxForm4(self, strs: List[str], m: int, n: int) -> int:
        print("Code4")
        #@lru_cache(maxsize = 128)
        def dfs(idx, m, n, memo):
            if idx == len(strs):
                return 0
            if (idx, m, n) in memo:
                return memo[(idx, m, n)]
            
            count0 = strs[idx].count("0")
            count1 = strs[idx].count("1")
            
            memo[(idx, m, n)] = dfs(idx + 1, m, n, memo)
            if count0 <= m and count1 <= n:
                countUse = 1 + dfs(idx + 1, m - count0, n - count1, memo)
                memo[(idx, m, n)] = max(memo[(idx, m, n)], countUse)
            return memo[(idx, m, n)]
        
        memo = {} 
        return dfs(0, m, n, memo)
    
    # 2022/05/23 
    # DFS [TLE]
    def findMaxForm4(self, strs: List[str], m: int, n: int) -> int:
            
        #@lru_cache(maxsize = 128)
        def dfs(idx, m, n):
            if idx == len(strs):
                return 0

            count0 = strs[idx].count("0")
            count1 = strs[idx].count("1")
                        
            if count0 <= m and count1 <= n:
                return max(dfs(idx + 1, m, n), 1 + dfs(idx + 1, m - count0, n - count1))
            else:
                return dfs(idx + 1, m, n)
        
        return dfs(0, m, n)
    
    #Top-Down DP + Precalulate matrixZeroOne + Better getMatrixZeroOne [O(len + m*n): 81%]
    def findMaxForm3(self, strs: List[str], m: int, n: int) -> int:
        print("Code3: Top-Down DP + Precalulate matrixZeroOne + Better getMatrixZeroOne")
    
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
    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        print("Code2: Top-Down DP + Precalulate matrixZeroOne ")
    
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
        print("Code1: Top-Down DP 1")
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