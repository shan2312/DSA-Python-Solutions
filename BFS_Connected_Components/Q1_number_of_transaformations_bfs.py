import collections

# BFS
def get_min_operations_bfs(start_num, target_num, additive_nums, multiplicative_nums):

    def get_neighbors(num):
        neighbors = [num * multiplicative_num for multiplicative_num in multiplicative_nums]
        neighbors.extend([num + additive_num for additive_num in additive_nums])
        return neighbors


    q = collections.deque([(start_num, 0)])
    seen = set()
    seen.add(start_num)

    while q:
        new_num, depth = q.popleft()
        
        if new_num == target_num:
            return depth
        elif new_num > target_num:
            continue
        neighbors = get_neighbors(new_num)
        
        for neighbor in neighbors:
            if neighbor not in seen:
                q.append((neighbor, depth + 1))
                seen.add(neighbor)

    return 0

if __name__ == "__main__":
    start_num = 3
    target_num = 80
    additive_nums =[1, 2]
    multiplicative_nums = [9, 6, 3]
    print(get_min_operations_bfs(start_num, target_num, additive_nums, multiplicative_nums))
