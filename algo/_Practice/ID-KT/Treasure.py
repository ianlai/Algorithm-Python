'''
======================================
[Problem-1] 兩點間是否能到 findLegalMoves

0可走, -1不可走

findLegalMoves(board, start1[0], start1[1])

     0  1  2  3  4
0  [ 0, 0, 0,-1,-1],
1  [ 0, 0,-1, 0, 0],
2  [ 0,-1, 0,-1, 0],
3  [ 0, 0,-1, 0, 0],
4  [ 0, 0, 0, 0, 0],
5  [ 0, 0, 0, 0, 0],
6  [ 0, 0, 0, 0, 0],

從一個點0,判斷是否能到另一個點0 
'''

grid = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def dfs(grid, cur, end, visited):
    if cur == end:
        return True
    if not (0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0])):
        return False
    if grid[cur[0]][cur[1]] == -1:
        return False
    if cur in visited:
        return False
    visited.add(cur)

    x, y = cur[0], cur[1]
    for nxt in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if dfs(grid, nxt, end, visited):
            return True
    return False

def findLegalMoves(grid, start, end):
    print("findLegalMoves", start, "->", end)
    if grid[end[0]][end[1]] == -1: #dst == -1 (not achivable)
        return False 

    visited = set()
    return dfs(grid, tuple(start), tuple(end), visited)    

print(findLegalMoves(grid, [5, 0], [1, 3])) #True
print(findLegalMoves(grid, [5, 0], [2, 2])) #False (no path)
print(findLegalMoves(grid, [5, 0], [1, 2])) #False (dst not achivable)


'''
Assume we need to return one path (any path) 
(1) 用這方法可以回傳一條任意path，但可以發現他走的非常崎嶇，並不是最短路徑(因為不是使用BFS)。
(2) 回傳的路徑假設想要用res來接，不能直接res = list(path)，因為這樣res的位置就被改掉了，傳進來參數就沒意義了。
    所以必須要使用extend或traverse+append一個一個加進去。
    在其他一些題目所以可以用res來存，是因為我們是要回傳全部路徑，這時候用res.append(list(path))就可以，因為沒有修改到res位置。
'''

def dfs_path(grid, cur, end, path, res, visited):
    if cur == end:
        # Incorrect! 
        #res = list(path) #res reference will be wiped and it won't keep the values
        path.append(cur)
        res.extend(path)
        return True
    if not (0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0])):
        return False
    if grid[cur[0]][cur[1]] == -1:
        return False
    if cur in visited:
        return False

    visited.add(cur)
    path.append(cur)
    x, y = cur[0], cur[1]
    for nxt in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if dfs_path(grid, nxt, end, path, res, visited):
            return True
    path.pop()
    return False

def findLegalMoves_path(grid, start, end):
    print("findLegalMoves_path", start, "->", end)
    if grid[end[0]][end[1]] == -1: #dst == -1 (not achivable)
        return []

    visited = set()
    res = []
    dfs_path(grid, tuple(start), tuple(end), [], res, visited)
    return res

print(findLegalMoves_path(grid, [5, 0], [1, 3])) #True
print(findLegalMoves_path(grid, [5, 0], [2, 2])) #False (no path)
print(findLegalMoves_path(grid, [5, 0], [1, 2])) #False (dst not achivable)

'''
======================================
[Problem-2] 是否能到全部的點 isReachable

實現isReachable(int[][] board, int x, int y)
還是同個board,問從(x, y)出發, 是否能到達所有的0

思路: 從給定點做DFS,紀錄抵達的0個數,和所有0個數相比。
'''

# Postorder DFS
def dfs(grid, x, y, visited):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return 0
    if grid[x][y] != 0:
        return 0
    if (x, y) in visited:
        return 0 
    visited.add((x, y))
    count = 1  # grid[x][y] == 1
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        count += dfs(grid, nx, ny, visited)
    return count 

def isReachable(grid, x, y):
    zeroCount = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                zeroCount += 1
    visited = set()
    zeroAchievable = dfs(grid, x, y, visited)
    #print(zeroCount, zeroAchievable)
    return zeroCount == zeroAchievable

grid1 = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

grid2 = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

grid3 = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, -1, -1, 0],
    [0, 0, 0, -1, 0],
    [-1, -1, 0, -1, 0],
    [0, 0, 0, 0, 0],
]

print(isReachable(grid1, 5, 0))  #False
print(isReachable(grid2, 5, 0)) #True
print(isReachable(grid3, 4, 0)) #True

'''
======================================
[Problem-3] 最短路徑

0可走, -1不可走, 1為鑽石
給起點和终點,問有没有一條不走回頭路的路線,能從起點走到终點,並拿走所有的鑽石,给出所有的最短路徑。
board3 = [
  [ 1, 0, 0, 0, 0 ],
  [ 0,-1,-1, 0, 0 ],
  [ 0,-1, 0, 1, 0 ],
  [-1, 0, 0, 0, 0 ],
  [ 0, 1,-1, 0, 0 ],
  [ 0, 0, 0, 0, 0 ],
]
'''


