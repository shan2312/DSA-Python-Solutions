from collections import deque

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
LAND = 1

def is_in_bounds(colors, row, col):
    num_rows, num_cols = len(colors), len(colors[0])

    is_row_in_bounds = row >= 0 and row < num_rows 
    is_col_in_bounds = col >= 0 and col < num_cols
    is_in_bounds = is_row_in_bounds and is_col_in_bounds

    return is_in_bounds



def get_island_area(start_row, start_col, seen, grid):
    area_of_island = 0

    if grid[start_row][start_col] != LAND:
        return area_of_island
    queue = deque([(start_row, start_col)])
    seen.add((start_row, start_col))
    
    while queue:
        current_row, current_col = queue.popleft()

        for delta_row, delta_col in directions:
            next_row, next_col = current_row + delta_row, current_col + delta_col
            
            if not is_in_bounds(grid, next_row, next_col): continue
            is_seen = (next_row, next_col) in seen

            if not is_seen and grid[next_row][next_col] == LAND:
                queue.append((next_row, next_col))
                seen.add((next_row, next_col))
        area_of_island += 1
    return area_of_island



def get_max_area_of_island(grid):
    num_rows, num_cols = len(grid), len(grid[0])
    
    seen = set()

    max_area_of_island = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) in seen:continue
            island_area = get_island_area(row, col, seen, grid)
            max_area_of_island = max(max_area_of_island, island_area)
                
    return max_area_of_island



if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(get_max_area_of_island(grid))