DIRECTIONS = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]

def get_neighbors(row, col, num_rows, num_cols):
    for row_change, col_change, direction in DIRECTIONS:
        neighbor_row, neighbor_col = row + row_change, col + col_change

        is_row_in_bounds = neighbor_row >= 0 and neighbor_row < num_rows
        is_col_in_bounds = neighbor_col >= 0 and neighbor_col < num_cols

        if not is_row_in_bounds or not is_col_in_bounds:
            continue
        yield (neighbor_row, neighbor_col, direction)

def get_all_paths(grid):
    paths = []
    num_rows, num_cols = len(grid), len(grid[0])
    target_row, target_col = num_rows-1, num_cols-1

    def get_all_paths_from(start_row, start_col, grid, visited_set, current_path):
        if start_row == target_row and start_col == target_col:
            paths.append(current_path[:])

        visited_set.add((start_row, start_col))

        for neighbor_row, neighbor_col, direction in get_neighbors(start_row, start_col, num_rows, num_cols):
            if (neighbor_row,neighbor_col) in visited_set or grid[neighbor_row][neighbor_col] == 0:
                continue
            current_path.append(direction)
            get_all_paths_from(neighbor_row, neighbor_col, grid, visited_set, current_path)
            current_path.pop()

        visited_set.remove((start_row, start_col))
    visited_set = set()
    get_all_paths_from(0, 0, grid, visited_set, [])
    return paths


print(get_all_paths([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]))
print(get_all_paths([
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
))

