class Solution:
    
    # 2022/06/15
    # LCS [O(MN): 22% / O(MN): 63%]
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(A, B):
            dp = [[0] * len(B) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B)):
                    if A[i] == B[j]:
                        if i == 0 or j == 0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        if i == 0 and j == 0:
                            dp[i][j] = 0
                        elif i == 0:
                            dp[i][j] = dp[i][j-1]
                        elif j == 0:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            return dp[-1][-1]
        return len(word1) + len(word2) - lcs(word1, word2) * 2