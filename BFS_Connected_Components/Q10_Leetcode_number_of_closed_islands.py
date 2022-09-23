from collections import deque

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
LAND = 0

def is_boundary_location(grid, row, col):
    first_row_index, first_col_index = 0, 0
    last_row_index, last_col_index = len(grid) - 1, len(grid[0]) - 1
    
    is_first_row, is_first_col = (row == first_row_index), (col == first_col_index)
    is_last_row, is_last_col = (row == last_row_index), (col == last_col_index)

    is_boundary = is_first_row or is_first_col or is_last_row or is_last_col
    return is_boundary

def is_in_bounds(grid, row, col):
    num_rows, num_cols = len(grid), len(grid[0])

    is_row_in_bounds = row >= 0 and row < num_rows 
    is_col_in_bounds = col >= 0 and col < num_cols
    is_in_bounds = is_row_in_bounds and is_col_in_bounds

    return is_in_bounds


def is_closed_island(grid, seen, start_row, start_col):

    queue = deque([(start_row, start_col)])
    seen.add((start_row, start_col))

    is_closed = True
    
    while queue:
        current_row, current_col = queue.popleft()
        is_boundary = is_boundary_location(grid, current_row ,current_col)

        if is_boundary:
                is_closed = False
                return is_closed

        for delta_row, delta_col in directions:
            next_row, next_col = current_row + delta_row, current_col + delta_col
            
            is_seen = (next_row, next_col) in seen

            if is_in_bounds(grid, next_row, next_col) and not is_seen and grid[next_row][next_col] == LAND:
                queue.append((next_row, next_col))
                seen.add((next_row, next_col))
    return is_closed


def count_closed_islands(grid):
    num_rows, num_cols = len(grid), len(grid[0])
    seen = set()
    
    count_of_closed_islands = 0                
    for row in range(num_rows):
        for col in range(num_cols):
            # We will only look at unexplored land which not in boundary locations
            if grid[row][col] == LAND and (row, col) not in seen and not is_boundary_location(grid, row, col):
                count_of_closed_islands += 1 if is_closed_island(grid, seen, row, col) else 0
                
    return count_of_closed_islands


if __name__ == "__main__":
    grid = [[1,1,1,1,1,1,1,0],
            [1,0,0,0,0,1,1,0],
            [1,0,1,0,1,1,1,0],
            [1,0,0,0,0,1,0,1],
            [1,1,1,1,1,1,1,0]]
    print(count_closed_islands(grid))

                
                    
                