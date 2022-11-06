from collections import defaultdict

def get_jumps_from_index(start_index, array, dp_cache):
    
    if start_index >= len(array) - 1:
        return 0

    if start_index in dp_cache:
        return dp_cache[start_index]
    
    maximum_jump_length_from_here = array[start_index]
    min_jumps_count_from_here = float('inf')

    
    for jump_length in range(1, maximum_jump_length_from_here + 1):
        next_index = start_index + jump_length
        count_jumps = 1 + get_jumps_from_index(next_index, array, dp_cache)
        min_jumps_count_from_here = min(min_jumps_count_from_here, count_jumps)

    dp_cache[start_index] = min_jumps_count_from_here

    return dp_cache[start_index]


def minNumberOfJumps(array):
    dp_cache = defaultdict(int)
    return get_jumps_from_index(0, array, dp_cache)
    