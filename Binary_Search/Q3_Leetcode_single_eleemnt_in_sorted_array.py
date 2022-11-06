
def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        
        mid = (left + right) // 2
        
        if nums[mid] == nums[mid + 1]:
            right_sub_array_size = right - mid + 1
            
            if right_sub_array_size % 2 != 0:
                left = mid
                
            else:
                right = mid - 1
                
        elif nums[mid] == nums[mid - 1]:
            left_sub_array_size = mid - left + 1
            
            if left_sub_array_size % 2 != 0:
                right = mid
                
            else:
                left = mid + 1
                
        else:
            return nums[mid]
        
    return nums[left]


if __name__ == '__main__':
    print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))