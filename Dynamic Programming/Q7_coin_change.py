from collections import defaultdict
from typing import List

def get_minimum_coins_for_amount(coins, amount):
    dp = defaultdict(int)

    def dfs_helper(current_index, remaining_amount):
        if (current_index, remaining_amount) in dp:
            return dp[current_index, remaining_amount]

        if remaining_amount == 0:
            return 0

        if remaining_amount < 0:
            return -1

        if current_index >= len(coins):
            return -1

        # Consider index
        with_index = dfs_helper(current_index, remaining_amount - coins[current_index])
        # Do not consider index
        without_index = dfs_helper(current_index + 1, remaining_amount)

        if with_index == -1 and without_index == -1:
            dp[current_index, remaining_amount] = -1
        elif with_index == -1:
            dp[current_index, remaining_amount] = without_index
        elif without_index == -1:
            dp[current_index, remaining_amount] = 1 + with_index
        else:
            dp[current_index, remaining_amount] = min(with_index + 1, without_index)

        return dp[current_index, remaining_amount]

    return dfs_helper(0, amount)


def get_minimum_coins_for_amount_1(coins, amount):
    count_coins = len(coins)

    dp = [[0 for _ in range(amount + 1)] for _ in range(count_coins + 1)]

    for j in range(1, len(dp[0])):
        dp[-1][j] = float('inf')

    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[0])):
            if j < coins[i]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i]], dp[i + 1][j])

    return -1 if dp[0][amount] == float('inf') else dp[0][amount]


def get_minimum_coins_for_amount_2(coins: List[int], amount: int) -> int:
    count_coins = len(coins)

    dp = [[0 for _ in range(amount + 1)] for _ in range(2)]

    for j in range(1, len(dp[0])):
        dp[count_coins % 2][j] = float('inf')

    for i in range(count_coins - 1, -1, -1):
        for j in range(len(dp[0])):
            if j < coins[i]:
                dp[i % 2][j] = dp[(i + 1) % 2][j]
            else:
                dp[i % 2][j] = min(1 + dp[i % 2][j - coins[i]], dp[(i + 1) % 2][j])

    return -1 if dp[0][amount] == float('inf') else dp[0][amount]


if __name__ == '__main__':
    print(get_minimum_coins_for_amount([1], 0))
