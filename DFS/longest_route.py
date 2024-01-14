# This problem cannot be memoized because state is not just the source, it also includes the visited_set


DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def get_neighbors(row, col, grid):
    num_rows, num_cols = len(grid), len(grid[0])

    for row_change, col_change in DIRECTIONS:
        neighbor_row, neighbor_col = row + row_change, col +col_change

        if neighbor_row < 0 or neighbor_row >= num_rows:
            continue

        if neighbor_col < 0 or neighbor_col >= num_cols:
            continue

        yield (neighbor_row, neighbor_col)


from collections import defaultdict
def get_longest_possible_route(grid, source, target):
    # cache = defaultdict(int)
    def get_longest_possible_route_from(grid, source, visited_set):
    
        if source == target:
            # cache[source] = 0
            return 0

        # if source in cache:
        #     print(source, cache[source])
        #     return cache[source]

        visited_set.add(source)
        
        max_path = -1*float('inf')
        for neighbor_row, neighbor_col in get_neighbors(source[0], source[1], grid):
            if (neighbor_row, neighbor_col) in visited_set or grid[neighbor_row][neighbor_col] == 0:
                continue
            max_path = max(max_path, (1 + get_longest_possible_route_from(grid, (neighbor_row, neighbor_col), visited_set)))
        visited_set.remove(source)

        # cache[source] = max_path
        return max_path

    visited_set = set()
    return get_longest_possible_route_from(grid, source, visited_set)
mat = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]

src = (0, 0)
dest = (5, 7)
print(get_longest_possible_route(mat, src, dest))