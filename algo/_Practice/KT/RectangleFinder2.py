'''
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
def rectangleFinder1(grid):
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


def rectangleFinder2(grid):
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

print("Grid1")
print(rectangleFinder1(grid1))
print(rectangleFinder2(grid1))
print(grid1)

print("Grid2")
print(rectangleFinder1(grid2))
print(rectangleFinder2(grid2))
print(grid2)