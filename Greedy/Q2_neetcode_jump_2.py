
# TC: O(N), SC: O(1)
def get_min_jumps_to_end(nums):
    l = r = 0
    res = 0

    while r < len(nums) - 1:
        farthest = 0

        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest
        res += 1

    return res


def get_min_jumps_to_end_top_down_dp(nums):
    
    def dfs_helper(index):
        if index >= len(nums) - 1:
            return 0
        
        min_jump = float('inf')
        for jump in range(1, nums[index] + 1):
            min_jump = min(min_jump, 1 + dfs_helper(index + jump))

        return min_jump
    
    return dfs_helper(0)


print(get_min_jumps_to_end_top_down_dp([2, 3, 1, 1, 4]))