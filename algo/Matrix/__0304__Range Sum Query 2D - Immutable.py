class NumMatrix:

    # 2022/02/15 
    # Prefix Sum [O(mn): 29%]
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefixSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    self.prefixSum[i][j] = matrix[i][j]
                else:
                    self.prefixSum[i][j] += self.prefixSum[i][j-1] + matrix[i][j] 
            
        for j in range(n):
            for i in range(m):
                if i == 0:
                    continue
                else:
                    self.prefixSum[i][j] += self.prefixSum[i-1][j]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefixSum = self.prefixSum
        res = prefixSum[row2][col2]
        if row1 == 0 and col1 == 0:
            return res
        elif row1 == 0:
            res -= prefixSum[row2][col1-1] 
        elif col1 == 0:
            res -= prefixSum[row1-1][col2]
        else:
            res += - prefixSum[row2][col1-1] - prefixSum[row1-1][col2] + prefixSum[row1-1][col1-1] 
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)