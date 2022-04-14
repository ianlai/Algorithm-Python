class Solution:
    
    # 2022/04/14
    # DP, add extra col and row for avoiding corner cases handling, reversed 
    # [Time:O(MN):88% / Space:O(MN):63%]
    # 
    # [3, 2, 1, 0]
    # [2, 2, 1, 0]
    # [2, 2, 1, 0]
    # [1, 1, 1, 0]
    # [1, 1, 1, 0]
    # [0, 0, 0, 0]
    # compare text1[i] == text2[j] 比較符合直覺
    # 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        print("Code5")
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # dp[i][j] means the LCS of text1[:i] and text2[:j] (i, j start from 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1 
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        for row in dp:
            print(row)
        return dp[0][0]
    
    
    # 2022/04/14
    # DP, add extra col and row for avoiding corner cases handling 
    # [Time:O(MN):88% / Space:O(MN):63%]
    # 
    # [0, 0, 0, 0]
    # [0, 1, 1, 1]
    # [0, 1, 1, 1]
    # [0, 1, 2, 2]
    # [0, 1, 2, 2]
    # [0, 1, 2, 3]
    # compare text1[i-1] == text2[j-1] 比較不符合直覺
    #
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        print("Code4")
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # dp[i][j] means the LCS of text1[:i] and text2[:j] (i, j start from 1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        for row in dp:
            print(row)
        return dp[m][n]
    
    # 2022/04/14
    # DP [Time:O(MN):88% / Space:O(MN):63%]
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        print("Code3")
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m-1][n-1]
    
    # 2022/03/09
    # Memoization [O(M*N2): 5%]
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        print("Code2")

        def helper(t1, t2, p1, p2, memo):
            if p1 == len(t1) or p2 == len(p2):
                return 0
            len1 = helper(t1, t2, p1+1, p2, memo)
            firstPos2 = t2.find(t1[p1], p2)
            len2 = helper(t1, t2, p1+1, firstPos2, memo) + 1
            memo[(p1, p2)] = max(len1, len2)
            return memo[(p1, p2)]
        memo = {}
        return self.helper(text1, text2, 0, 0, memo)

    # ==========================================================
        
    # 2021/07/20
    # Memoization [12%]
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        print("Code1")
        if not text1 or not text2:
            return 0
        
        memo = {}
        return self.helper(text1, text2, 0, 0, memo)
        #return self.helper1(text1, text2, memo)
        
    def helper(self, text1, text2, p1, p2, memo):
        if (p1, p2) in memo:
            return memo[(p1, p2)]   
        
        if p1 >= len(text1) or p2 >= len(text2):
            return 0
        
        count = 0
        try:
            idx2 = text2.index(text1[p1], p2)
        except ValueError:
            count = self.helper(text1, text2, p1+1, p2, memo)
            memo[(p1, p2)] = count
            return count 
    
        a = self.helper(text1, text2, p1+1, idx2+1, memo) + 1
        b = self.helper(text1, text2, p1+1, p2, memo)
        
        count = max(a, b) 
        memo[(p1, p2)] = count
        return count 
            
    def helper1(self, text1, text2, memo):
        if not text1 or not text2:
            return 0
        
        if (text1, text2) in memo:
            return memo[(text1, text2)]  
        
        count = 0
        try:
            idx2 = text2.index(text1[0])
        except ValueError:
            count = self.helper1(text1[1:], text2, memo)
            memo[(text1, text2)] = count
            return count 
    
        a = self.helper1(text1[1:], text2[idx2+1:], memo) + 1
        b = self.helper1(text1[1:], text2, memo)
        
        # if a >= b:
        #     print("a >= b")
        # else:
        #     print("a <  b")
        # print("  ", a, text1[1:], text2[idx2+1:])
        # print("  ", b, text1[1:], text2)
        
        count = max(a, b) 
        memo[(text1, text2)] = count
        return count 