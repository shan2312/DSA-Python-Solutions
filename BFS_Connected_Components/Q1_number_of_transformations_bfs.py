from collections import deque
import queue

INITIAL_COUNT_OF_OPERATIONS = 0
CANNOT_REACH_TARGET = -1

def get_next_nums_list(num, additive_nums, multiplicative_nums):
    next_nums_from_multiplication = [num * multiplicative_num for multiplicative_num in multiplicative_nums]
    next_nums_from_addition = [num + additive_num for additive_num in additive_nums]
    
    next_nums_from_multiplication.extend(next_nums_from_addition)
    next_nums_list = next_nums_from_multiplication

    return next_nums_list



def get_min_operations_to_target(start_num, target_num, additive_nums, multiplicative_nums):

    queue = deque([(start_num, INITIAL_COUNT_OF_OPERATIONS)])
    seen = set()
    seen.add(start_num)

    while queue:
        num_so_far, count_operations_so_far = queue.popleft()
        
        if num_so_far == target_num:
            return count_operations_so_far
        elif num_so_far > target_num:
            continue
        
        next_nums_list = get_next_nums_list(num_so_far, additive_nums, multiplicative_nums)
        
        for next_num in next_nums_list:
            if next_num in seen: continue
            queue.append((next_num, count_operations_so_far + 1))
            seen.add(next_num)

    return CANNOT_REACH_TARGET

if __name__ == "__main__":
    start_num = 3
    target_num = 80
    additive_nums =[1, 2]
    multiplicative_nums = [9, 6, 3]
    print(get_min_operations_to_target(start_num, target_num, additive_nums, multiplicative_nums))
