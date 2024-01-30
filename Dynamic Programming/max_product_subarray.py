
# TC: O(N), SC: O(1)
def get_max_product_subarray(nums):
    prefix = suffix = 1
    max_prod = -1 * float('inf')

    for i in range(len(nums)):
        if prefix == 0:prefix = 1
        if suffix == 0: suffix = 1

        prefix *= nums[i]
        suffix *+ nums[len(nums) - i - 1]
        max_prod = max(max_prod, prefix, suffix)

    return max_prod

def get_max_product_subarray_1(nums):
    cur_min = cur_max = 1
    res = -1 * float('inf')

    for num in nums:
        if num == 0: 
            cur_min = cur_max = 1
            continue
        
        cur_min, cur_max = min(cur_min * num, cur_max * num, num), max(cur_min * num, cur_max * num, num)
        res = max(res, cur_max)

    return res

print(get_max_product_subarray_1([3, 2, -1, 4]))

