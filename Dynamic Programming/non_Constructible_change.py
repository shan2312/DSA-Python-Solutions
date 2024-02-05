def nonConstructibleChange(coins):
    maxAmount = sum(coins)
    amountCache = [False] * (maxAmount + 1)
    amountCache[0] = True

    for coinsIdx in range(1, len(coins) + 1):
        for amountIdx in range(len(amountCache) - 1, -1, -1):
            if amountIdx - coins[coinsIdx - 1] < 0:
                continue
            amountCache[amountIdx] |= amountCache[amountIdx - coins[coinsIdx - 1]]

    for change, isConstructible in enumerate(amountCache):
        if not isConstructible:
            return change
    return maxAmount + 1
        


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))