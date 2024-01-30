from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    count_of_coins = len(coins)

    for i in range(count_of_coins - 1, -1, -1):
        for j in range(len(dp)):
            if j < coins[i]:
                continue
            dp[j] += dp[j - coins[i]]

    return dp[-1]


if __name__ == '__main__':
    print(change(5, [1, 2, 5]))
