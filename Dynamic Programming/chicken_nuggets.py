def is_chicken_nugget_possible(N):
    dp = [False] * (N + 1)
    dp[0] = True

    for i in range(1, len(dp)):
        if i < 3:
            dp[i] = False
        elif i < 4:
            dp[i] = dp[i - 3]

        elif i < 7:
            dp[i] = dp[i - 3] or dp[i - 4]

        else:
            dp[i] = dp[i - 3] or dp[i - 4] or dp[i - 7]

    return dp[-1]


print(is_chicken_nugget_possible(39))

