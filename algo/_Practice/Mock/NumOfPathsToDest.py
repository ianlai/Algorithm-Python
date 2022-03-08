from turtle import down


def num_of_paths_to_dest(n):
  dp = [[0 for _ in range(n)] for _ in range(n)]
  dp[0][0] = 1
  for i in range(n):
    for j in range(n):
      if i > j:  
        if j == 0:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = dp[i-1][j] + dp[i][j-1]
      elif i == j and i > 0:
        dp[i][j] = dp[i][j-1]
  return dp[n-1][n-1]



Divide and conquer 
DP


先找基本沒障礙的
DFS
Top-down 
Buttom-Up 




function numOfPathsToDest(n):
    # allocate a 2D array for memoization
    memo = [][]

    # the memoization array is initialized with -1
    # to indicate uncalculated squares.
    for i from 0 to n-1:
        for j from 0 to n-1:
            memo[i][j] = -1

    return numOfPathsToSquare(n-1, n-1, memo)


# input:
#    i, j - a pair of non-negative integer coordinates
#    memo - a 2D memoization array.
# output:
#    number of paths from (0,0) to the square represented in (i,j),

function numOfPathsToSquare(i, j, memo):
    if (i < 0 OR j < 0):
        return 0
    else if (i < j):
        memo[i][j] = 0
    else if (memo[i][j] != -1):
        return memo[i][j] 
    else if (i == 0 AND j == 0):
        memo[i][j] = 1
    else:
        memo[i][j] = numOfPathsToSquare(i, j -1, memo) +
        numOfPathsToSquare(i - 1, j, memo)

    return memo[i][j]