class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_sum = 0
        prefix_sum_to_index = {0: -1}

        for index, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % k

            if (
                prefix_sum in prefix_sum_to_index
                and (index - prefix_sum_to_index[prefix_sum]) >= 2
            ):
                return True

            if prefix_sum not in prefix_sum_to_index:
                prefix_sum_to_index[prefix_sum] = index

        return False
