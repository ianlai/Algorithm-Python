'''
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