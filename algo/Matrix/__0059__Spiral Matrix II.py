class Solution:
    
    # 2022/04/13
    # Matrix [O(n2): 60%]
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        def nextPoint(i, j, d):
            if d == 'r':
                if j + 1 == n or res[i][j+1] != 0:
                    return i+1, j, 'd'
                return i, j+1, 'r'
            elif d == 'd':
                if i + 1 == n or res[i+1][j] != 0:
                    return i, j-1, 'l'
                return i+1, j, 'd'
            elif d == 'l':
                if j - 1 == -1 or res[i][j-1] != 0:
                    return i-1, j, 'u'
                return i, j-1, 'l'
            elif d == 'u':
                if i - 1 == -1 or res[i-1][j] != 0:
                    return i, j+1, 'r'
                return i-1, j, 'u'
            
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        row, col, direction = 0, 0, 'r'
        for val in range(1, n * n + 1):
            res[row][col] = val
            row, col, direction = nextPoint(row, col, direction)
        return res 
            