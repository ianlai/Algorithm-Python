class Solution:
    
    # DP [O(n3): 15%]
    def mctFromLeafValues(self, arr: List[int]) -> int:
        m = len(arr)
        dp = [[0 for _ in range(m)] for _ in range(m)]

                
        for d in range(1, m):
            for i in range(m):
                if i+d >= m:
                    continue

                ### Correct (compare all possible division)
                minVal = float('inf')
                for p in range(d):
                    ll, lr = i, i+p
                    rl, rr = i+p+1, i+d
                    minVal = min(minVal, dp[ll][lr] + dp[rl][rr] + max(arr[ll:lr+1]) * max(arr[rl:rr+1]))
                dp[i][i+d] = minVal
                
                ### Wrong (compare only left and right two possibilities)
                left  = dp[i][i+d-1] + max(arr[i:i+d]) * arr[i+d]
                right = dp[i+1][i+d] + max(arr[i+1:i+d+1]) * arr[i]
                #dp[i][i+d] = min(left, right)
                #print(i,",",i+d,":",left, right, minVal)
                
        
        # for i in range(m):
        #     print(dp[i])
        
        return dp[0][m-1]