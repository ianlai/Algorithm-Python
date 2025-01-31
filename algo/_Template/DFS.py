
m, n = len(grid), len(grid[0])
def dfs(x, y, cur, res, visited):
    if x == m-1 and y == n-1:
        res.append(list(cur))
        return 
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:                
        if not (0 <= nx < m and 0 <= ny < n):
            continue 
        if (nx, ny) in visited:
            continue 
        cur.append([nx, ny])
        visited.add((nx, ny))
        dfs(nx, ny, cur, res, visited)
        visited.remove((nx, ny))
        cur.remove([nx, ny])
    return 

visited = set()
visited.add((0,0))
dfs(0, 0, [0, 0], 0, visited)