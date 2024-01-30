# TC: O(N*M), SC: O(N*M)
def get_num_unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]

    dp[m - 1][n - 1] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m -1 and j == n - 1:
                continue
            if (i + 1) >= m:
                dp[i][j] = dp[i][j + 1]
            elif (j + 1) >= n:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]

# TC: O(N^2), SC: O(N)
def get_num_unique_paths_opt(m, n):
    dp = [1] * n

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[j] += dp[j + 1]

    return dp[0]


print(get_num_unique_paths_opt(3, 7))