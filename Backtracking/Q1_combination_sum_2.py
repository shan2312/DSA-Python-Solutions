
# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [[1,1,6],[1,2,5],[1,7],[2,6]]
# [1 1 2 5 6 7 10]

#        1    1  2 5           6    7   10
#       1 2 5      6, 7, 10  7 10   10

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

def get_combinations_that_sum_to_target(candidates, target):
    candidates.sort()
    result = []
    
    def helper(start, combination_so_far, sum_so_far, candidates, target, result):
        
        if sum_so_far == target:
            result.append(combination_so_far[:])
            return 

        if start >= len(candidates) or sum_so_far > target:
            return

        for index in range(start, len(candidates)):
            if index > start and candidates[index] == candidates[index - 1]:
                continue

            combination_so_far.append(candidates[index])
            helper(index + 1, combination_so_far, sum_so_far + candidates[index], candidates, target, result)
            combination_so_far.pop()

    helper(0, [], 0, candidates, target, result)
    return result


if __name__ == '__main__':
    print(get_combinations_that_sum_to_target([10,1,2,7,6,1,5], 8))

        
        