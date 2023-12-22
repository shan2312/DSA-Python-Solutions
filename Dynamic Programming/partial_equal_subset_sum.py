def can_partition(nums):
    if sum(nums) % 2:
        return False

    target = sum(nums)//2

    dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[0])):
            if j < nums[i]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[1][2] = (dp[i + 1][j - nums[i]]) or (dp[i + 1][j])

    return dp[0][-1]



if __name__ == '__main__':
    print(can_partition([1, 2, 5]))