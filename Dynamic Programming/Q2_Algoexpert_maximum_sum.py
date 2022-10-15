
########## Recursion with memoization ##############
########## O(n) space-time complexity ##############
from collections import defaultdict

def get_maximum_sum_from_ith_index(array, start_index, dp_cache):
    if start_index >= len(array):
        return 0

    if start_index in dp_cache:
        return dp_cache[start_index]

    # Consider start index
    first_max = get_maximum_sum_from_ith_index(array, start_index + 2,dp_cache)
    first_max += array[start_index]

    # Do not Consider start index
    second_max = get_maximum_sum_from_ith_index(array, start_index + 1, dp_cache)

    dp_cache[start_index] = max(first_max, second_max)
    return dp_cache[start_index]


def maxSubsetSumNoAdjacent(array):
    dp_cache = defaultdict(int)
    return get_maximum_sum_from_ith_index(array, 0, dp_cache)


########## Dynamic programming      ##############
########## O(n) time and O(1) space ##############

def maxSubsetSumNodeAdjacent_dp(array):
    second, first = array[0], max(array[1], array[0])

    for index in range(2, len(array)):
        current = max(first, second + array[index])
        second = first
        first = current

    return first


##### Dynamic programming, return numbers also ###
########## O(n) time and O(1) space ##############
## TODO

if __name__ == '__main__':
    print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
    print(maxSubsetSumNodeAdjacent_dp([7, 10, 12, 7, 9, 14]))

    
