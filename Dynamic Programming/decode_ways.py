# Bottom up, O(N)
def get_num_ways(s):
    def is_valid(s):
        s_int = int(s)
        return s_int > 0 and s_int < 27

    dp = [0] * (len(s) + 1)
    dp[-1] = 1

    for i in range(len(dp) - 2, -1, -1):
        if not is_valid(s[i]):
            continue

        if (i + 2) >= len(dp):
            dp[i] = dp[i + 1]
            continue

        dp[i] = dp[i + 1] + (dp[i + 2] if is_valid(s[i: (i + 2)]) else 0)

    return dp[0]


def get_num_ways_top_down(s):
    def is_valid(s):
        s_int = int(s)
        return s_int > 0 and s_int < 27

    def dfs_helper(index):
        if index >= len(s):
            return 1

        num_ways_1 = 0
        num_ways_2 = 0
        if is_valid(s[index]):
            num_ways_1 = dfs_helper(index + 1)

        
            if (index + 2) <= len(s) and is_valid(s[index: (index + 2)]):
                num_ways_2 = dfs_helper(index + 2)

        return num_ways_1 + num_ways_2

    return dfs_helper(0)



print(get_num_ways_top_down('21238207'))