from collections import defaultdict
def numbersInPi(pi, numbers):
    numbers_set = set(numbers)
    dp = defaultdict(int)
    
    def dfs(index):
        if index in dp:
            print('DP hit')
            return dp[index]
            
        if index >= len(pi):
            return -1

        min_spaces = float('inf')
        for i in range(index + 1, len(pi) + 1):
            if pi[index:i] in numbers_set:
                min_spaces = min(min_spaces, 1 + dfs(i))
        dp[index] = min_spaces
        return dp[index]
    ans = dfs(0)
    return ans if ans != float('inf')  else -1


def nums_in_pi_iterative(pi, numbers):
    numbers_set = set(numbers)
    dp = [float('inf')]*(len(pi) + 1)

    dp[-1] = -1

    for i in range(len(dp) - 2, -1, -1):
        for j in range(i + 1, len(dp)):
            if pi[i:j] in numbers_set:
                dp[i] = min(dp[i], 1 + dp[j])

    return dp[0]


print(numbersInPi('31456789', ['3','1', '4', '5', '6', '7', '8', '9', '1456789', '456789', '314', '456', '789']))
print(nums_in_pi_iterative('31456789', ['3','1', '4', '5', '6', '7', '8', '9', '1456789', '456789', '314', '456', '789']))

