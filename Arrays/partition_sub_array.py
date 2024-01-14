# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.


# TC: O(N), SC: O(N)
def get_min_partition_length(arr):
    max_elements = [arr[0]]
    for index in range(1, len(arr)):
        max_elements.append(max(max_elements[-1], arr[index]))

    min_elements = [arr[-1]]
    for index in range(len(arr) - 2, -1, -1):
        min_elements.append(min(min_elements[-1], arr[index]))

    for index, (min_element, max_element) in enumerate(zip(min_elements[::-1][1:], max_elements[:-1])):
        if max_element <= min_element:
            return (index + 1)
        
    return len(arr)

# TC: O(N), SC:O(1)
def get_min_partition_length_optimised(arr):
    partition_index = 0
    max_till_now = temp = arr[0]

    for index in range(1, len(arr)):
        if arr[index] < max_till_now:
            partition_index = index
            max_till_now = temp

        else:
            temp = max(temp, arr[index])

    return partition_index + 1



print(get_min_partition_length([5,0,3,8,6]))
print(get_min_partition_length_optimised([5,0,3,8,6]))

        