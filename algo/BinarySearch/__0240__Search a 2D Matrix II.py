class Solution:
    
    # Use concept of Binary Search ; remove one row or col each time [O(M+N), 81%]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        M, N = len(matrix), len(matrix[0])
        row, col = 0, len(matrix[0]) - 1 
        
        while not (row >= M or col < 0):
            rightUp = matrix[row][col]
            if rightUp == target:
                return True
            if rightUp < target:
                row += 1
            if rightUp > target: 
                col -= 1
        return False