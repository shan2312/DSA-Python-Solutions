# Question:  You are given an array with n elements. Identify the number of sub-arrays from this array which has all the elements that are present in the original array.
from collections import defaultdict

def get_count_sub_arrays_with_same_elements(nums):
    left = count = 0
    count_distinct_elements = len(set(nums))
    hashmap = defaultdict(int)

    for right in range(len(nums)):
        hashmap[nums[right]] += 1

        while len(hashmap) == count_distinct_elements:
            hashmap[nums[left]] -= 1
            if hashmap[nums[left]] == 0:
                del hashmap[nums[left]]
            left += 1
            count += len(nums) - right

    return count

print(get_count_sub_arrays_with_same_elements([1, 2, 3, 1, 6, 2, 1]))