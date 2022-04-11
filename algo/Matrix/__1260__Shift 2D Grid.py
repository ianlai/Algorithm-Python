class Solution:
    
    # 2022/04/11
    # Matrix, convert the point to new point [O(m*n): 26%]
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        res = [[0] * n for _ in range(m)]
        
        def convert(i, j, k):
            newPoint = (i * n + j + k) % total 
            ni, nj = newPoint // n, newPoint % n 
            return ni, nj
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ni, nj = convert(i, j, k)
                res[ni][nj] = grid[i][j]
                
        return res
    