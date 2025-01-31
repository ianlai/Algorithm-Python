class Solution:
    
    # 2021/01/25 
    # Tabular DP [O(n2): 32%]
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        
        startMap = collections.defaultdict(list)
        for start, end, tip in rides:
            startMap[start].append((end, tip))
        
        for start in range(n):
            for end, tip in startMap[start]:
                dp[end] = max(dp[end], dp[start] + end - start + tip)
            dp[start + 1] = max(dp[start + 1], dp[start])
            
        return dp[n]