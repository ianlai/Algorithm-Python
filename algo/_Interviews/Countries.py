# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N, M = len(A), len(A[0])
    visited = set()
    count = 0 
    for i in range(N):
        for j in range(M):
            if (i, j) not in visited:
                dfs(A, i, j, visited)
                count += 1
    return count

def dfs(A, i, j, visited):
    N, M = len(A), len(A[0])
    # if not (0 <= i < N and 0 <= j < M):
    #     return 
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if A[ni][nj] != A[i][j]:
            continue
        if (ni, nj) in visited:
            continue
        visited.add((ni, nj))
        dfs(A, ni, nj, visited)





