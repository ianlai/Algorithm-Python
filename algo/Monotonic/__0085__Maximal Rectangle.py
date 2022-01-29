class Solution:
    
    # Prefix Sum + Monotonic Stack [O(MN + N): 23%]
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        row = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if j == 0:
                    row[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '0':
                    row[i][j] = 0
                else:
                    row[i][j] = row[i][j-1] + int(matrix[i][j])
        
        # Find largest histogram
        res = 0 
        for j in range(n):
            col = [r[j] for r in row]
            res = max(res, self.largestRectangleArea(col))
            
        return res 
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        mstack = [-1]
        maxArea = 0
        for i, v in enumerate(heights):
            curIdx = 0
            while mstack[-1] != -1  and heights[mstack[-1]] >= v:
                curIdx = mstack.pop()
                area = (i - mstack[-1] - 1) * heights[curIdx]
                maxArea = max(maxArea, area)
                #print("(1) ", curIdx - 1, i, heights[curIdx], "->", maxArea)
            mstack.append(i)
        
        #print(mstack)
        while mstack[-1] != -1:
            rightIdx = mstack.pop()
            rightHeight = heights[rightIdx]
            leftIdx = mstack[-1]
            area = (len(heights) - leftIdx - 1) * rightHeight
            maxArea = max(maxArea, area)    
        #print(heights, "->", maxArea)
        return maxArea