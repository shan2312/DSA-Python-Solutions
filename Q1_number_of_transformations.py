import collections
def get_min_operations(start_num, target_num, additive_nums, multiplicative_nums):
    memo = collections.defaultdict(int)
    def helper(current_num):
        if current_num in memo:
            return memo[current_num]
        
        if current_num == target_num:
            return 0
        
        if current_num > target_num:
            return float('inf')
        
        # Add a number
        min_count_add = float('inf')
        for add_num in additive_nums:
            new_num = add_num + current_num
            min_count_add = min(min_count_add, 1 + helper(new_num))
                
        # Multiply a number
        min_count_mul = float('inf')
        for mul_num in multiplicative_nums:
            new_num = mul_num * current_num
            min_count_mul = min(min_count_mul, 1 + helper(new_num))
            
        memo[current_num]  = min(min_count_add, min_count_mul)
        return memo[current_num]
    return helper(start_num)


if __name__ == "__main__":
    start_num = 3
    target_num = 80
    additive_nums =[1, 2]
    multiplicative_nums = [9, 6, 3]
    print(get_min_operations(start_num, target_num, additive_nums, multiplicative_nums))