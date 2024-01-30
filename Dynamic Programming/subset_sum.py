# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9


def is_subset_sum_to_target(arr, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(dp) - 1, -1, -1):
            if j < arr[i]:
                continue
            dp[j] |= dp[j - arr[i]] 

    return dp[-1]

print(is_subset_sum_to_target([3, 34, 4, 12, 5, 2], 39))