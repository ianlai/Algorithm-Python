class Solution:
    
    # 2022/01/25
    # Memoization DP [O(): 81%]
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        def dfs(s, start, end, memo):
            if start > end:
                return 0
            if start == end:
                return 1 
            if (start, end) in memo:
                return memo[(start, end)]
            
            count = 0
            if s[start] != s[end]:
                count = max(dfs(s, start, end - 1, memo), dfs(s, start + 1, end, memo))
            else:
                count = max(count, dfs(s, start + 1, end - 1, memo) + 2)
                    
            memo[(start, end)] = count
            return count
                
        memo = {}
        return dfs(s, 0, len(s) - 1, memo)