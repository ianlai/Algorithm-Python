'''

n = 5
            [x, x, x, x, o] -> end
            [x, x, x, o, o]
            [x, x, o, o, o]
            [x, o, o, o, o]
  start ->  [o, o, o, o, o]

'''

def num_of_paths_to_dest5(n):
    dp = [1] * n
    for i in range(1, n):  # row
        for j in range(i+1, n):  # col
            dp[j] = dp[j] + dp[j-1]

    return dp[n-1]


def num_of_paths_to_dest4(n):
    print("Code4")
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        for j in range(n):
            if j > i:
                break
            if j == 0:
                continue
            else:
                dp[j] = dp[j] + dp[j-1]
        print(i, dp)
    return dp[-1]


def num_of_paths_to_dest3(n):
    print("Code3")
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = 1
    for i in range(1, n):
        if i >= 2:
            dp[0] = dp[1]
        for j in range(n):
            if j > i:
                break
            if j == 0:
                dp[1][j] = dp[0][j]
            else:
                dp[1][j] = dp[0][j] + dp[1][j-1]
        print(i, dp)
    return dp[1][-1] if n > 1 else 1

# ======================================


def num_of_paths_to_dest2(n):
    print("Code2")
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if j > i:
                break
            if i % 2 == 0:
                if j == 0:
                    dp[0][j] = dp[1][j]
                else:
                    dp[0][j] = dp[1][j] + dp[0][j-1]
            else:
                if j == 0:
                    dp[1][j] = dp[0][j]
                else:
                    dp[1][j] = dp[0][j] + dp[1][j-1]
        print(i, dp)
    return max(dp[0][-1], dp[1][-1])

def num_of_paths_to_dest1(n):
    print("Code1")
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i > j:
                if j == 0:
                    dp[i % 2][j] = dp[(i-1) % 2][j]
                else:
                    dp[i % 2][j] = dp[(i-1) % 2][j] + dp[i % 2][j-1]
            elif i == j and i > 0:
                dp[i % 2][j] = dp[i % 2][j-1]
    return dp[n % 2-1][n-1]


# Time:  O(n2)
# Space: O(n2)
def num_of_paths_to_dest0(n):
    print("Code0")
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                if i == 0:
                    dp[i][j] = 1
                if i > 0:
                    dp[i][j] = dp[i-1][j]
            elif i < j:
                if i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

print(num_of_paths_to_dest0(5))
print(num_of_paths_to_dest1(5))
print(num_of_paths_to_dest5(5))
