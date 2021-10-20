class Solution:
    
    #DP [O(M*N): 31%]
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        row = [list(matrix[i]) for i in range(m)]
        col = [list(matrix[i]) for i in range(m)]
        acu = [list(matrix[i]) for i in range(m)]
        
        for i in range(len(row)):
            for j in range(len(row[0])):
                if j == 0:
                    continue
                if row[i][j] != 0:
                    row[i][j] += row[i][j-1]
        
        for i in range(len(col)):
            if i == 0:
                continue
            for j in range(len(col[0])):
                if col[i][j] != 0:
                    col[i][j] += col[i-1][j]
        
        count = 0
        for i in range(len(acu)):
            for j in range(len(acu[0])):
                if matrix[i][j] == 1:
                    acu[i][j] = min(row[i][j], col[i][j])
                if i > 0 and j > 0:
                    acu[i][j] = min(acu[i-1][j-1] + 1, acu[i][j])
                count += acu[i][j]
        
        # print("---mat---")
        # for r in matrix:
        #     print(r)
        # print("---row---")
        # for r in row:
        #     print(r)
        # print("---col---")
        # for r in col:
        #     print(r)
        # print("---acu---")
        # for r in acu:
        #     print(r)
    
        return count