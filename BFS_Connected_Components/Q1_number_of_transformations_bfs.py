from collections import deque

INITIAL_COUNT_OF_OPERATIONS = 0
CANNOT_REACH_TARGET = -1

def get_neighbors(number, additive_nums, multiplicative_nums):

    for number_to_add in additive_nums:
        next_num = number + number_to_add
        yield next_num

    for number_to_multiply in multiplicative_nums:
        next_num = number * number_to_multiply
        yield next_num



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
        
        
        for next_num in get_neighbors(num_so_far, additive_nums, multiplicative_nums):
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
