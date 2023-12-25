# TC: O(N), SC: O(1)
def is_jump_possible(nums):
    goal = len(nums) - 1


    for i in range(len(nums) - 1, -1, -1):
        next_jump_index = i + nums[i]
        if next_jump_index >= goal:
            goal = i

    return goal == 0

def is_jump_possible_top_down_dp(nums):
    dp = {}
    def dfs_helper(index):
        if index >= len(nums):
            return True 
        
        if index in dp:
            return dp[index]
        
        for jump in range(1, nums[index] + 1):
            if dfs_helper(index + jump):
                dp[index] = True
                return dp[index]
        dp[index] = False
        return dp[index]
    
    return dfs_helper(0)

def is_jump_possible_bottom_up_dp(nums):
    dp = [False] * (len(nums))
    dp[-1] = True

    for i in range(len(dp) - 1, -1, -1):
        for jump in range(nums[i] + 1):
            if (i + jump) >= len(dp):
                dp[i] = True
                continue
            dp[i] |= dp[i + jump]

    return dp[0]
            







if __name__ == '__main__':
    print(is_jump_possible_bottom_up_dp([2, 2, 1, 1, 4]))