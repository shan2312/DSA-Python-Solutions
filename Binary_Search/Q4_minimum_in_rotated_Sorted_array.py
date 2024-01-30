# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Minimum element in an array - O(N)
# Minimum element in a sorted array - O(1)

# Minimum element in rotated sorted array - O(NLogN)

from typing import List

class Solution:
    def findMinimumInRotatedSortedArray(self, nums: List[int]) -> int:

        leftIdx, rightIdx = 0, len(nums) - 1

        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            
            midValue, rightValue = nums[midIdx], nums[rightIdx]

            isLeftSubArray = (midValue > rightValue)
            isRightSubArray = (midValue < rightValue)

            if isLeftSubArray:
                leftIdx = midIdx + 1

            elif isRightSubArray: 
                rightIdx = midIdx
                
            else:
                return rightValue

if __name__ == '__main__':
    s = Solution()
    print(s.findMinimumInRotatedSortedArray([4,2,4,4,4,4]))

