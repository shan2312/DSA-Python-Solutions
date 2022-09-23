import collections

CANNOT_REACH_TARGET = INFINITE = float('inf')
TARGET_REACHED = 0

def get_min_operations_to_target(start_num, target_num, additive_nums, multiplicative_nums):

    cached_min_operations = collections.defaultdict(int)

    def get_min_operations_to_target_helper(current_num):

        if current_num in cached_min_operations:
            return cached_min_operations[current_num]
        
        if current_num == target_num:
            return TARGET_REACHED
        
        if current_num > target_num:
            return CANNOT_REACH_TARGET
        
        # Add a number
        count_if_addition = INFINITE
        for additive_num in additive_nums:
            new_num = additive_num + current_num
            count_if_addition = min(count_if_addition, 1 + get_min_operations_to_target_helper(new_num))
                
        # Multiply a number
        count_if_multiplication = CANNOT_REACH_TARGET
        for multiplicative_num in multiplicative_nums:
            new_num = multiplicative_num * current_num
            count_if_multiplication = min(count_if_multiplication, 1 + get_min_operations_to_target_helper(new_num))
            
        cached_min_operations[current_num]  = min(count_if_addition, count_if_multiplication)
        return cached_min_operations[current_num]

    return get_min_operations_to_target_helper(start_num)


if __name__ == "__main__":
    start_num = 3
    target_num = 80
    additive_nums =[1, 2]
    multiplicative_nums = [9, 6, 3]
    print(get_min_operations_to_target(start_num, target_num, additive_nums, multiplicative_nums))