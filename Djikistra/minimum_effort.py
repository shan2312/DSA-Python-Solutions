import heapq

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def get_neighbors(row, col, heights):
    num_rows, num_cols = len(heights), len(heights[0])
    for row_change, col_change in DIRECTIONS:
        neighbor_row, neighbor_col = (row + row_change), (col + col_change)
        
        is_row_in_bounds = neighbor_row >= 0 and neighbor_row < num_rows
        is_col_in_bounds = neighbor_col >= 0 and neighbor_col < num_cols
        
        if not is_row_in_bounds: continue
        if not is_col_in_bounds: continue
            
        yield (neighbor_row, neighbor_col)
    
def minimumEffortPath(heights):
    num_rows, num_cols = len(heights), len(heights[0])
    
    min_effort_heap = [(0, 0, 0)]
    distance_dict = {(row, col): {'distance': float('inf'), 'previous': None} for row in range(num_rows) for col in range(num_cols)}
    distance_dict[(0, 0)]['distance'] = 0
    
    while min_effort_heap:
        min_effort, curr_row, curr_col = heapq.heappop(min_effort_heap)
        current_height = heights[curr_row][curr_col]
        
        for neighbor_row, neighbor_col in get_neighbors(curr_row, curr_col, heights):
            neighbor_height = heights[neighbor_row][neighbor_col]
            max_diff = max(distance_dict[(curr_row, curr_col)]['distance'], abs(neighbor_height - current_height))

            if max_diff < distance_dict[(neighbor_row, neighbor_col)]['distance']:
                distance_dict[(neighbor_row, neighbor_col)]['distance'] = max_diff
                distance_dict[(neighbor_row, neighbor_col)]['previous'] = (curr_row, curr_col)
                heapq.heappush(min_effort_heap, (max_diff, neighbor_row, neighbor_col))

    path = get_path(distance_dict, (num_rows - 1, num_cols - 1))
    return path, distance_dict[(num_rows - 1, num_cols - 1)]['distance']

def get_path(distance_dict, destination):
    path = []
    while destination is not None:
        path.append(destination)
        destination = distance_dict[destination]['previous']

    path.reverse()
    return path
    
    
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))

heights = [[1,2,3],[3,8,4],[5,3,5]]
print(minimumEffortPath(heights))

heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPath(heights))