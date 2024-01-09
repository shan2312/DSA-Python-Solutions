

def solve_knapsack(weights, profits, max_weight):
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(len(weights) + 1)]
    
    for j in range(len(dp[0])):
        dp[-1][j] = 0

    
    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[0])):
            if j < weights[i]:
                dp[i][j] = dp[i + 1][j]
                continue

            dp[i][j] = max(dp[i + 1][j - weights[i]] + profits[i], dp[i + 1][j])
     
    return dp[0][-1]


def solve_knapsack_optimized(weights, profits, max_weight):
    dp = [0] * (max_weight + 1)

    for i in range(len(weights) - 1, -1, -1):
        for j in range(len(dp) - 1, -1, -1):
            if j < weights[i]:
                continue

            dp[j] = max(dp[j - weights[i]] + profits[i], dp[j])
     
    return dp[-1]


print(solve_knapsack_optimized([4, 5, 1], [1, 2, 3], 4))