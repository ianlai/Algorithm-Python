class Solution:
    
    # 2022/06/02
    # Matrix manipulation (assign to new matrix) [O(MN): 45% / O(1): 16%]
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix