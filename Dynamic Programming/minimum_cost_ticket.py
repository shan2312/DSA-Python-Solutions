def get_min_cost_to_travel(days, costs):
    days_set = set(days)
    dp = [0] * (max(days) + 1)

    for i in range(len(dp) - 1, -1, -1):
        if i not in days_set:
            dp[i] = dp[i + 1] if (i + 1) < len(dp) else 0
            continue

        dp[i] = min(
                    costs[0] + (dp[i + 1] if (i + 1) < len(dp) else 0),
                    costs[1] + (dp[i + 7] if (i + 7) < len(dp) else 0),
                    costs[2] + (dp[i + 30] if (i + 30) < len(dp) else 0)
        )
    return dp[1]


if __name__ == '__main__':
    print(get_min_cost_to_travel([1, 4, 6, 7, 8, 20], [2, 7, 15]))
