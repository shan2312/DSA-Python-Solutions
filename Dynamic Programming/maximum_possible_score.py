from collections import defaultdict

def get_maximum_possible_score(arr, k):
    dp = defaultdict(float)
    def get_maximum_possible_score_from(index, k, arr):
        if index in dp:
            return dp[index]
        if index >= len(arr):
            return 0

        max_score = -1*float('inf')
        for i in range(1, k + 1):
            max_score = max(max_score, arr[index] + get_maximum_possible_score_from(index + i, k, arr))

        dp[index] = max_score
        return dp[index]

    return get_maximum_possible_score_from(0, k, arr)



print(get_maximum_possible_score([100, -30, -50, -15, -20, -30], 3))

print(get_maximum_possible_score([-44, -17, -54, 79], 2))