class Solution:
    
    # 2022/02/08
    # Use set to store row and col [O(n): 57%]
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroRow = set()
        zeroCol = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in zeroRow or j in zeroCol:
                    matrix[i][j] = 0