def solve_unbounded_knapsack(values, weights, max_weight):
    dp = [0] * (max_weight + 1)

    for i in range(len(weights) - 1, -1, -1):
        for j in range(len(dp)):
            if j < weights[i]:
                continue
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[-1]


print(solve_unbounded_knapsack([1, 30], [1, 50], 100))