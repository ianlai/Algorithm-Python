class Solution:
    
    # DP - One dimension [23%]
    def numSquares(self, n: int) -> int:
        largestPerfectRoot = floor(sqrt(n))
        dp = [ inf for _ in range(n+1)]
        sarr = [i ** 2 for i in range(1, largestPerfectRoot + 1)]
        
        for i in range(n + 1):
            for j in range(1, largestPerfectRoot + 1):
                j -= 1
                idx = i - sarr[j]
                if idx < 0:
                    break
                elif idx == 0:
                    dp[i] = 1
                    break
                else:
                    dp[i] = min(dp[i], dp[idx] + 1)
        return dp[-1]
    
    
    # DP - Two dimensions [TLE]
    def numSquares2(self, n: int) -> int:
        largestPerfectRoot = floor(sqrt(n))
        dp = [[ 0 for _ in range(largestPerfectRoot)] for _ in range(n+1)]
        
        for i in range(n + 1):
            for j in range(1, largestPerfectRoot + 1):
                perfectSqure = j ** 2
                j -= 1
                if j == 0:
                    dp[i][j] = i
                else:
                    idx = i - perfectSqure
                    if idx < 0:
                        dp[i][j] = dp[i][j-1]
                    elif idx == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1], dp[idx][j] + 1)
        return dp[-1][-1]
    
    # DP - Two dimensions [TLE]
    def numSquares1(self, n: int) -> int:
        largestPerfectRoot = floor(sqrt(n))
        dp = [[ inf for _ in range(n+1)] for _ in range(largestPerfectRoot)]
        
        for i in range(largestPerfectRoot):
            perfectSqure = (i + 1) ** 2
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                else:
                    idx = j - perfectSqure
                    if idx < 0:
                        dp[i][j] = dp[i-1][j]
                    elif idx == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][idx] + 1)
        return dp[-1][-1]