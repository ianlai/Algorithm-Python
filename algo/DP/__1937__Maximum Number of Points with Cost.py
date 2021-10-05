class Solution:
    
    #DP [O(n2): 32%] 
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        dpl = [[0 for _ in range(n)] for _ in range(m)]
        dpr = [[0 for _ in range(n)] for _ in range(m)]
        dpl[0] = points[0]
        dpr[0] = points[0]
        
        for i in range(1, m):
            #Left 
            for j in range(n):
                if j == 0:
                    dpl[i][j] = points[i][j] + dpl[i-1][j]
                else:
                    up = points[i][j] + dpl[i-1][j]
                    dpl[i][j] = max(up, dpl[i][j-1] + points[i][j] - points[i][j-1] - 1) 
            #Right
            for j in range(n-1, -1, -1):
                if j == n - 1:
                    dpr[i][j] = points[i][j] + dpr[i-1][j]
                else:
                    up = points[i][j] + dpr[i-1][j]
                    dpr[i][j] = max(up, dpr[i][j+1] + points[i][j] - points[i][j+1] - 1)
                    
                #Update dpr and dpl 
                dpr[i][j] = max(dpr[i][j], dpl[i][j])
                dpl[i][j] = dpr[i][j]

        return max(dpr[-1])
    
    #===============================================
    
    #DP [O(n3): TLE] 
    def maxPointsSlow(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = list(points[0])
        
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = max(dp[i][j] , dp[i-1][k] - abs(k-j) + points[i][j])
                    
        print("Correct:")                    
        for row in dp:
            print(row)
        return max(dp[-1])