
# Naive top down DP: O(n!) after memoization O(2^n)
from functools import lru_cache
from collections import defaultdict

@lru_cache(None)
def get_max_coins(balloons):

    if len(balloons) == 0:
        return 0
    

    max_coins = 0
    for index in range(len(balloons)):
        coins = balloons[index - 1] * balloons[index] * balloons[index + 1] if (index - 1) >= 0 and (index + 1) < len(balloons) \
        else balloons[index - 1] * balloons[index] if (index - 1) >= 0 else balloons[index] * balloons[index + 1] if (index + 1) < len(balloons) else balloons[index]

        max_coins = max(max_coins, coins + get_max_coins([b for i, b in enumerate(balloons) if i != index]))

    return max_coins

# Optimised approach - O(N^3)
def get_max_coins_top_down(balloons):
    memo = defaultdict(int)
    def get_max_coins_from(left, right):
        if (left, right) in memo:
            return memo[(left, right)]
        
        if left > right:
            return 0
        
        max_coins = 0
        for index in range(left, right + 1):
            coins = balloons[left - 1] * balloons[index] * balloons[right + 1] if (left - 1) >= 0 and (right + 1) < len(balloons) \
        else balloons[left - 1] * balloons[index] if (left - 1) >= 0 else balloons[index] * balloons[right + 1] if (right + 1) < len(balloons) else balloons[index]
            
            max_coins = max(max_coins, coins + get_max_coins_from(left, index - 1) + get_max_coins_from(index + 1, right))
        memo[(left, right)] = max_coins
        return memo[(left, right)]
    
    return get_max_coins_from(0, len(balloons) - 1)


# Optimised approach - O(N^3), SC: O(N^2)
def get_max_coins_bottom_up(balloons):
    dp = [[0] * len(balloons) for _ in range(len(balloons))]


    for left in range(len(balloons) - 1, -1, -1):
        for right in range(left, len(balloons)):
            for index in range(left, right + 1):
                gain = balloons[left - 1] * balloons[index] * balloons[right + 1] if (left - 1) >= 0 and (right + 1) < len(balloons) \
        else balloons[left - 1] * balloons[index] if (left - 1) >= 0 else balloons[index] * balloons[right + 1] if (right + 1) < len(balloons) else balloons[index]
                
                remaining = dp[left][index - 1] if (index - 1) >= 0 else 0 + dp[index + 1][right] if (index + 1) < len(dp) else 0
                dp[left][right] = max(remaining + gain, dp[left][right])

    return dp[0][-1]



print(get_max_coins_bottom_up([3, 1, 5, 8]))
print(get_max_coins_bottom_up([1, 5]))