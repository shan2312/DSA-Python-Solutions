# Duplicates need to be taken care of
class Solution:
    def get_first_position_to_swap(self, arr):
        first_swap_pos = len(arr) - 2
        
        
        while first_swap_pos >= 0 and arr[first_swap_pos] <= arr[first_swap_pos + 1]:
            first_swap_pos -= 1
        return first_swap_pos
    
    def get_second_position_to_swap(self, arr, first_swap_pos):
        second_swap_pos = len(arr) - 1
        
        while second_swap_pos > first_swap_pos and arr[second_swap_pos] >= arr[first_swap_pos]:
            second_swap_pos -= 1
            
        while arr[second_swap_pos] == arr[second_swap_pos - 1]:
            second_swap_pos -= 1
        
        return second_swap_pos
            
    def prevPermOpt1(self, arr):
        
        first_pos = self.get_first_position_to_swap(arr)
        
        if first_pos == -1:
            return
        
        second_pos = self.get_second_position_to_swap(arr, first_pos)
        
        arr[first_pos], arr[second_pos] = arr[second_pos], arr[first_pos]


if __name__ == '__main__':
    s = Solution()
    arr = [3, 1, 2]
    s.prevPermOpt1(arr)
    print(arr)