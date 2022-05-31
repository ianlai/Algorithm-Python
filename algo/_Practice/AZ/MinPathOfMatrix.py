
'''
Input:
[
    [51 , 24 , 19*, 10*],
    [18*, 12*, 23*, 40 ],
    [60 , 19 , 67 , 42 ]
]

Output: 82 
82 = 18 + 12 + 23 + 19 + 10
'''
from math import inf

grid1 = [  #82
    [51 , 24 , 19 , 10 ],
    [18 , 12 , 23 , 40 ],
    [60 , 19 , 67 , 42 ]
]

grid2 = [  #146
    [51 ,  5,  19 , 15, 96 ],
    [18 , 12 , 63 , 17, 88 ],
    [60 , 74 , 19 ,  6, 79 ],
    [60 , 59 , 12 , 21, 33 ]
]


'''
  Code1: Backtracking
  TC: O(2^(MN))

  - 不是一次traverse的題目，要找path，不是找點，所以不能直接碰到visited就跳出
  - 因此必須要做backtracking，visitied必須要存入再取出，也必須記住目前的path
  - 因此這方法的判斷式就必須要包在for裡面

  - 不能用memo，因為memo通常是一個點碰到就離開，但我們其實要繼續往下找，來更新此點的最小值
'''
def dfs(grid, cur, visited, memo):
    m, n = len(grid), len(grid[0])
    r, c = cur[-1]

    if c == len(grid[0]) - 1:
        return grid[r][c]
    # if memo[r][c] != inf:
    #     return memo[r][c]
        
    res = inf
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1)]:
        if not (0 <= nr < m and 0 <= nc < n):
            continue 
        if visited[nr][nc]:
            continue
        visited[nr][nc] = True
        res = min(res, dfs(grid, cur + [(nr, nc)], visited, memo))
        visited[nr][nc] = False

    res += grid[r][c]
    memo[r][c] = res
    #print(r, c, res)
    return res

def findMinPathOfMatrix1(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    memo = [[inf] * n for _ in range(m)]
    res = inf
    for row in range(m):
       res = min(res, dfs(grid, [(row, 0)], visited, memo))
    # for row in memo:
    #     print(row)
    return res

print(findMinPathOfMatrix1(grid1))
print(findMinPathOfMatrix1(grid2))

'''
  Code2: DP
  TC: 
'''
def findMinPathOfMatrix2(grid):
    m, n = len(grid), len(grid[0])

    return