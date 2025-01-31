class Solution:
    
    #DP [Time O(M*N):25% / Space: 34%]
    def countSquares(self, matrix: List[List[int]]) -> int:
        print("Method-2")
        m, n = len(matrix), len(matrix[0])
        acu = [list(matrix[i]) for i in range(m)]
        
        count = 0
        for i in range(len(acu)):
            for j in range(len(acu[0])):
                if matrix[i][j] == 0:
                    continue
                if i > 0 and j > 0:
                    minLastSquareSize = min(acu[i-1][j], acu[i][j-1], acu[i-1][j-1])
                    acu[i][j] = minLastSquareSize + 1
                else:
                    acu[i][j] = 1
                count += acu[i][j]
                
#         print("---mat---")
#         for row in matrix:
#             print(row)
#         print("---acu---")
#         for row in acu:
#             print(row)
        return count
    
    #DP [Time O(M*N): 6% / Space: 8%]
    def countSquares(self, matrix: List[List[int]]) -> int:
        print("Method-1")
        
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