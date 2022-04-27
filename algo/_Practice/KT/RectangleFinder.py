'''
======================================
[Problem-1] 找唯一的一個長方形

There is an image filled with 0s and 1s. 
There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.

Input: 
[
    [1,1,1,1,1,1],
    [1,1,1,0,0,0],
    [1,1,1,0,0,0],
    [1,1,1,1,1,1]
]
Output: 
    [(1,3),(2,5)]
'''
grid1 = [
    [1,1,1,1,1,1],
    [1,1,1,0,0,0],
    [1,1,1,0,0,0],
    [1,1,1,1,1,1]
]

grid2 = [
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,0,0,0,0,1],
    [1,0,0,0,0,1]
]

grid3 = [
]

def rectangleFinder(grid):
    print("(1) 找單個長方形")
    if len(grid) == 0 or len(grid[0]) == 0:
        return []

    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                down, right = i, j
                for row in range(i, len(grid)):
                    if grid[row][j] == 0:
                        down = row
                for col in range(j, len(grid[0])):
                    if grid[i][col] == 0:
                        right = col
                res.append((i, j))
                res.append((down, right))
                return res
    return res

print(rectangleFinder(grid1))
print(rectangleFinder(grid2))
print(rectangleFinder(grid3))


'''
======================================
[Problem-2] 找多個長方形

For the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s. 
The rectangles are separated by 1s. Find all the rectangles.

Input: 
grid1 = [
    [1,1,1,1,1,1],
    [1,1,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,1,1,1]
]
Output: 
    [[(1,3),(2,5)], [(2,0),(3,1)]]
'''
grid1 = [
    [1,1,1,1,1,1],
    [1,1,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,1,1,1]
]

grid2 = [
    [1,0,0,1,0,1],
    [1,1,1,1,1,1],
    [1,0,0,0,0,1],
    [1,0,0,0,0,1]
]

grid3 = [
]

print("--------------------")
def rectangleFinder2(grid):
    print("(2) 找多個長方形")
    if len(grid) == 0 or len(grid[0]) == 0:
        return []

    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                down, right = i, j
                for row in range(i, len(grid)):
                    if grid[row][j] != 0:
                        break
                    for col in range(j, len(grid[0])):
                        if grid[row][col] == 0:
                            grid[row][col] = '#'
                            right = max(right, col)
                        else:
                            break
                    down = max(down, row)
                res.append([(i, j),(down, right)])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                grid[i][j] = 0
    return res

print("Grid1:", grid1)
print(rectangleFinder2(grid1))

print("Grid2:", grid2)
print(rectangleFinder2(grid2))

'''
======================================
[Problem-3] 找多個不規則形狀

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

print("--------------------")

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
    print("(3) 找多個不規則形狀")
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

