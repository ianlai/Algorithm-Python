'''
The image has random shapes filled with 0s, separated by 1s. Find all the shapes. 
Each shape is represented by coordinates of all the elements inside.

Input: 
    grid1 = [
        [1,1,1,1,1,1],
        [1,1,1,0,0,1],
        [0,0,0,0,1,0],
        [0,0,1,1,0,0]
    ]
Output: 
    [
        [(1,3), (1,4), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1)], 
        [(2,5), (3,4), (3,5)]
    ]
'''

grid1 = [
    [1,1,1,1,1,1],
    [1,1,1,0,0,1],
    [0,0,0,0,1,0],
    [0,0,1,1,0,0]
]

def dfs(grid, row, col, cur, shapes):
    m, n = len(grid), len(grid[0])
    if not (0 <= row < m and 0 <= col < n):
        return 
    if grid[row][col] != 0:
        return 
    cur.append((row, col))
    grid[row][col] = 1 #visited
    for ni, nj in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        dfs(grid, ni, nj, cur, shapes)

def findShapes(grid):
    shapes = []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            cur = []
            dfs(grid, i, j, cur, shapes)
            if len(cur) > 0:
                shapes.append(cur)
    return shapes

shapes = findShapes(grid1)
print(shapes)

