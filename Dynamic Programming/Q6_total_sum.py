

def get_num_ways_for_target(nums, target):
    nums_sum = sum(nums)
    num_size = len(nums)

    if target > nums_sum or target < -1* nums_sum:
        return 0

    dp = [[0 for _ in range(target - nums_sum, target + nums_sum + 1)] for _ in range(num_size + 1)]
    dp[-1][nums_sum - target] = 1

    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[0])):
            if j < nums[i]:
                dp[i][j] = dp[i + 1][j + nums[i]]
            elif (j + nums[i]) >= len(dp[0]):
                dp[i][j] = dp[i+ 1][j - nums[i]]
            else:
                dp[i][j] = dp[i + 1][j + nums[i]] + dp[i + 1][j - nums[i]]

    return dp[0][nums_sum]

def get_num_ways_for_target_1(nums, target):
    nums_sum = sum(nums)
    num_size = len(nums)

    if target > nums_sum or target < -1* nums_sum:
        return 0

    dp = [[0 for _ in range(target - nums_sum, target + nums_sum + 1)] for _ in range(2)]
    dp[num_size%2][nums_sum - target] = 1

    for i in range(num_size - 1, -1, -1):
        for j in range(len(dp[0])):
            if j < nums[i]:
                dp[i % 2][j] = dp[(i + 1) % 2][j + nums[i]]
            elif (j + nums[i]) >= len(dp[0]):
                dp[i % 2][j] = dp[(i + 1) % 2][j - nums[i]]
            else:
                dp[i % 2][j] = dp[(i + 1) % 2][j + nums[i]] + dp[(i + 1) % 2][j - nums[i]]

    return dp[0][nums_sum]


if __name__ == '__main__':
    print(get_num_ways_for_target_1([1, 1, 1, 1, 1], 3))
