class Solution:
    
    '''
    2
    3 4
    6 5 7
    4 1 8 3
    '''
    '''
    由上往下可以用array交換，就不需要用mod
    由下往上不用做min，更方便。
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        print("2022/06/13 由下往上")
        m = len(triangle)
        dp = triangle[-1]
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
    '''
    T.C. = O(M^2)
    S.C. = O(M) 
    '''
    def minimumTotal6(self, triangle: List[List[int]]) -> int: 
        print("2022/06/13 ")
        m = len(triangle)
        dp = [[0] * m for _ in range(2)]
        #dp0 = [0] * m
        #dp1 = [0] * m
        dp[0][0] = triangle[0][0]
        
        for i in range(1, m):
            for j in range(m):
                if j > i:
                    break
                    
                dp[i%2][j] = triangle[i][j]
                if j == i:
                    dp[i%2][j] += dp[(i-1)%2][j-1] 
                elif j == 0:
                    dp[i%2][j] += dp[(i-1)%2][j]
                else:
                    dp[i%2][j] += min(dp[(i-1)%2][j-1], dp[(i-1)%2][j])
                    
        return min(dp[1]) if m % 2 == 0 else min(dp[0]) 
    
    '''
    T.C. = O(M^2)
    S.C. = O(M^2) 
    '''
    def minimumTotal5(self, triangle: List[List[int]]) -> int: 
        print("2022/06/13")
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, m):
            for j in range(m):
                if j > i:
                    break
                    
                dp[i][j] = triangle[i][j]
                if j == i:
                    dp[i][j] += dp[i-1][j-1] 
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])
                
        return min(dp[m-1])
                
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # =========================================================
    # Bottom-up DP with rolling array [time: O(n2): 19% / space: 65%]
    def minimumTotal4(self, triangle: List[List[int]]) -> int: 
        print("Bottom-up DP; (i, j) defined as min path to top, rolling array to save storage")
        if not triangle:
            return 0
        
        n = len(triangle) 
        dp = [[0 for j in range(n)] for i in range(2)]
        for i in range(n):
            for j in range(i+1):
                if j == 0: 
                    dp[i%2][j] = triangle[i][j] + dp[(i-1)%2][j]
                elif j == i:
                    dp[i%2][j] = triangle[i][j] + dp[(i-1)%2][j-1]
                else:
                    dp[i%2][j] = min(dp[(i-1)%2][j-1], dp[(i-1)%2][j]) + triangle[i][j]
        return min(dp[i%2])
    
    # =========================================================
    # Bottom-up DP [time: O(n2): 19% / space: 15%]
    def minimumTotal3(self, triangle: List[List[int]]) -> int: 
        print("Bottom-up DP; (i, j) defined as min path to top")
        if not triangle:
            return 0
        
        n = len(triangle) 
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if j == 0: 
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[n-1])
        
    # =========================================================
    # Top-down DP, (i, j) defined as min path to bottom [time: O(n2), 26% / space: 8%]
    def minimumTotal2(self, triangle: List[List[int]]) -> int: 
        print("Top-down DP; (i, j) defined as min path to bottom")
        if not triangle:
            return 0
        
        n = len(triangle) 
        memo = {}
        return self.minPath2(triangle, 0, 0, memo)
    
    def minPath2(self, triangle, i, j, memo):
        n = len(triangle)
        if (i, j) in memo:
            return memo[(i, j)]
        if not (0 <= i < n and 0 <= j < len(triangle[i])):
            return 0
        left  = self.minPath2(triangle, i+1, j, memo)
        right = self.minPath2(triangle, i+1, j+1, memo)      
        memo[(i, j)] = min(left, right) + triangle[i][j]
        return memo[(i, j)]
        
    # =========================================================
    # Top-down DP, using a special status to record out of boundary [O(n2), 9%]
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        print("Top-down DP; (i, j) defined as min path to top")
        if not triangle:
            return 0
        
        n = len(triangle) 
        memo = {}
        results = []
        
        for j in range(n):
            #print("-------")
            #print(m-1, j)
            results.append(self.minPath1(triangle, n-1, j, memo))
        return min(results)
    
    def minPath1(self, triangle, i, j, memo):
        n = len(triangle)
        #print(">" , i , j)
        if (i, j) in memo:
            return memo[(i, j)]
        if not (0 <= i < n and 0 <= j < len(triangle[i])):
            return "x"
        left  = self.minPath1(triangle, i-1, j-1, memo)
        right = self.minPath1(triangle, i-1, j, memo)
                
        result = 0
        if left == "x" and right == "x": 
            result = triangle[i][j]
        elif left != "x" and right != "x":
            result = triangle[i][j] + min(left, right)
        elif left != "x" and right == "x":
            result = triangle[i][j] + left 
        elif right != "x" and left == "x":
            result = triangle[i][j] + right             
        #print(">>", i, j, ":", result)
        memo[(i, j)] = result
        return result
        