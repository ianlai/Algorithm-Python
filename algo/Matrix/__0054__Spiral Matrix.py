class Solution:

    # 2022/02/15
    # Matrix [O(m*n): 25%]
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        print("Code1")
        res = []
        m, n = len(matrix), len(matrix[0])        
        curDir = 0
        i, j = 0, 0
        row_u, row_d = -1, m
        col_l, col_r = -1, n
        while len(res) < m * n:
            if row_u < i < row_d and col_l < j < col_r:
                res.append(matrix[i][j])
                if curDir == 0:
                    j += 1
                elif curDir == 1:
                    i += 1
                elif curDir == 2:
                    j -= 1
                else:
                    i -= 1
            else:
                if curDir == 0:
                    row_u += 1
                    j -= 1
                    i += 1
                elif curDir == 1:
                    col_r -= 1
                    i -= 1
                    j -= 1
                elif curDir == 2:
                    row_d -= 1
                    j += 1
                    i -= 1
                else:
                    col_l += 1
                    i += 1
                    j += 1
                curDir += 1
                curDir %= 4
        return res