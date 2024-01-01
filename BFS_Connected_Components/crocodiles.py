

from collections import defaultdict, deque
import math

def compute_squared_distance(point_one, point_two):
    x_one, y_one = point_one
    x_two, y_two = point_two

    return (x_one - x_two)**2 + (y_one - y_two)**2

def build_graph(crocodiles, r):
    graph = defaultdict(list)
    for croc1_id, position1 in enumerate(crocodiles):
        for croc2_id, position2 in enumerate(crocodiles):
            if croc1_id == croc2_id: continue
            
            distance = compute_squared_distance(position1, position2)
            if distance > 4*(r**2): continue
            graph[croc1_id].append(croc2_id)
            graph[croc2_id].append(croc1_id)

    return graph
    

def get_bounds_of_crocodile_group(starting_croc_id, adjacency_dict, visited_set, crocodile_positions):

    queue = deque([starting_croc_id])
    visited_set.add(starting_croc_id)

    min_x = max_x = crocodile_positions[starting_croc_id][0]
    min_y = max_y = crocodile_positions[starting_croc_id][1]

    while queue:
        current_node = queue.popleft()

        min_x = min(min_x, crocodile_positions[current_node][0])
        max_x = max(max_x, crocodile_positions[current_node][0])
        min_y = min(min_y, crocodile_positions[current_node][1])
        max_y = max(max_y, crocodile_positions[current_node][1])
        
        for neighbor in adjacency_dict[current_node]:
            if neighbor in visited_set: continue
            queue.append(neighbor)
            visited_set.add(neighbor)

    return min_x, max_x, min_y, max_y

def is_pond_covered(min_x, max_x, min_y, max_y, r, W, H):
    is_left_or_top_blocked = min_x <= r or (H - max_y) <= r
    is_right_or_down_clocked = min_y <= r or (W - max_x) <= r
    
    return is_left_or_top_blocked and is_right_or_down_clocked


def can_fish_reach(position_crocodiles, r, W, H):
    adjacency_dict = build_graph(position_crocodiles, r)

    visited_set = set()
    for crocodile_id in adjacency_dict:
        if crocodile_id in visited_set: continue
        min_x, max_x, min_y, max_y = get_bounds_of_crocodile_group(crocodile_id, adjacency_dict, visited_set, position_crocodiles)
        if is_pond_covered(min_x, max_x, min_y, max_y, r, W, H):
            return False
        
    return True



print(can_fish_reach([[0, 0.5],[0.3, 0.5], [0.6, 0.5], [0.9, 0.5]], 0.3, 1, 1))