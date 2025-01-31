'''
======================================
[Problem-1] Valid matrix
給一個N*N的矩陣，判定是否是有效矩陣。
有效矩陣的定義是每一行或每一列的數字都必須正好是1到N的數。輸出一個bool。
'''

def validateMatrix(matrix):
    print("(1) validateMatrix")
    m, n = len(matrix), len(matrix[0])
    if m != n:
        raise Exception("Not square")

    for i in range(m):
        for j in range(n):
            if not (1 <= matrix[i][j] <= n):
                return False
    return True

matrix1 = [[1, 3, 1, 1, 5],
           [4, 4, 2, 2, 1],
           [4, 3, 3, 2, 3],
           [1, 3, 2, 4, 5],
           [5, 5, 5, 1, 5]
           ]

matrix2 = [[1, 3, 1, 1, 5],
           [4, 4, 2, 2, 1],
           [4, 3, 3, 2, 3],
           [1, 3, 2, 4, 5],
           [6, 5, 5, 1, 5]
           ]
matrix3 = [[1, 3, 1, 1, 5],
           [4, 4, 2, 2, 1],
           [4, 3, 0, 2, 3],
           [1, 3, 2, 4, 5],
           [3, 5, 5, 1, 5]
           ]

print(validateMatrix(matrix1))
print(validateMatrix(matrix2))
print(validateMatrix(matrix3))


'''
======================================
[Problem-2] Valid nonogram

A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions. 
Specifically, each cell can be either black or white, which we will represent as 0 for black and 1 for white.

+------------+
| 1  1  1  1 |
| 0  1  1  1 |
| 0  1  0  0 |
| 1  1  0  1 |
| 0  0  1  1 |
+------------+

For each row and column, the instructions give the lengths of contiguous runs of black (0) cells. 
For example, the instructions for one row of [ 2, 1 ] indicate that there must be a run of two black cells, 
followed later by another run of one black cell, and the rest of the row filled with white cells.

These are valid solutions: [ 1, 0, 0, 1, 0 ] and [ 0, 0, 1, 1, 0 ] and also [ 0, 0, 1, 0, 1 ]
This is not valid: [ 1, 0, 1, 0, 0 ] since the runs are not in the correct order.
This is not valid: [ 1, 0, 0, 0, 1 ] since the two runs of 0s are not separated by 1s.

Your job is to write a function to validate a possible solution against a set of instructions. 
Given a 2D matrix representing a player's solution; and instructions for each row along with additional instructions for each column; 
return True or False according to whether both sets of instructions match.

### Example instructions #1

matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]

rows1_1    =  [], [1], [1,2], [1], [2]
columns1_1 =  [2,1], [1], [2], [1]
validateNonogram(matrix1, rows1_1, columns1_1) => True

Example solution matrix:
matrix1 ->
                                   row
                +------------+     instructions
                | 1  1  1  1 | <-- []
                | 0  1  1  1 | <-- [1]
                | 0  1  0  0 | <-- [1,2]
                | 1  1  0  1 | <-- [1]
                | 0  0  1  1 | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
  column       [2,1] | [2] |
  instructions      [1]   [1]
'''


def validateNonogram(matrix, row, col):
    m, n = len(matrix), len(matrix[0])
    print("(2) validateNonogram")
    # valid row
    for i in range(m):
        part = 0
        reset = False
        for j in range(n):
            if part >= len(row[i]):
                leftZero = 0
            else:
                leftZero = row[i][part]

            if matrix[i][j] == 0:
                reset = True
                if leftZero > 0:
                    leftZero -= 1
                else:
                    print("row invalid: ", i, j, "part:", part)
                    return False
            else:
                if reset:
                    part += 1
                    reset = False

    # valid col
    for j in range(n):
        part = 0
        reset = False
        for i in range(m):
            if part >= len(col[j]):
                leftZero = 0
            else:
                leftZero = col[j][part]

            if matrix[i][j] == 0:
                reset = True
                if leftZero > 0:
                    leftZero -= 1
                else:
                    print("col invalid: ", i, j, "part:", part)
                    return False
            else:
                if reset:
                    part += 1
                    reset = False
    return True


matrix1 = [[1, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 0],
           [1, 1, 0, 1],
           [0, 0, 1, 1]]
rows1 = [[], [1], [1, 2], [1], [2]]
columns1 = [[2, 1], [1], [2], [1]]
print(validateNonogram(matrix1, rows1, columns1))

print()

matrix2 = [[1, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 0],
           [1, 1, 0, 1],
           [0, 0, 1, 0]]
rows2 = [[], [1], [1, 2], [1], [2, 1]]
columns2 = [[2, 1], [1], [2], [1]]
print(validateNonogram(matrix2, rows2, columns2))
