class Solution:
    
    # Top-down DP, using a special status to record out of boundary [O(m*n), 9%]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        m, n = len(triangle), len(triangle)
        memo = {}
        results = []
        
        # for i in range(m):
        #     print(triangle[i])
        
        for j in range(n):
            #print("-------")
            #print(m-1, j)
            results.append(self.minPath(triangle, m-1, j, memo))
        return min(results)
    
    def minPath(self, triangle, i, j, memo):
        m, n = len(triangle), len(triangle[0])
        #print(">" , i , j)
        if (i, j) in memo:
            return memo[(i, j)]
        if not (0 <= i < m and 0 <= j < len(triangle[i])):
            return "x"
        left  = self.minPath(triangle, i-1, j-1, memo)
        right = self.minPath(triangle, i-1, j, memo)
                
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
        