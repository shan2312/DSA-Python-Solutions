# arr can have duplicates. Duplication will not be a problem because we are going to ensure that the increasing order of second half after swapping
class Solution:
    def get_first_number_to_swap(self, nums):
        first_swap_pos = len(nums) - 2
        
        while first_swap_pos >=0 and nums[first_swap_pos] >= nums[first_swap_pos + 1]:
            first_swap_pos -= 1
            
        return first_swap_pos
    
    def get_second_number_to_swap(self, nums, first_swap_pos):
        second_swap_pos = len(nums) - 1
        
        while second_swap_pos > first_swap_pos and nums[second_swap_pos] <= nums[first_swap_pos]:
            second_swap_pos -= 1
            
        return second_swap_pos
        
    def reverse_from(self, nums, start):
        end = len(nums) - 1
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def nextPermutation(self, nums):
        first_pos = self.get_first_number_to_swap(nums)
        
        if first_pos == -1:
            nums.reverse()
            return
        
        second_pos = self.get_second_number_to_swap(nums, first_pos)
        
        nums[first_pos], nums[second_pos] = nums[second_pos], nums[first_pos]
        
        
        first_pos += 1
        self.reverse_from(nums, first_pos)



if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 3]
    s.nextPermutation(arr)
    print(arr)
    
        
        
        