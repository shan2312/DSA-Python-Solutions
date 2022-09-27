def find_peak_element(nums):
    if not nums:
        return 

    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
    
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    print(find_peak_element([2,4,8, 5]))

