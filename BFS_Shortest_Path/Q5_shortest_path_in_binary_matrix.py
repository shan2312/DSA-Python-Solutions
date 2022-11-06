DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
INFINITY = float("inf")
CANNOT_REACH_END = -1

from collections import deque


class Solution:
    def get_neighbors(self, row, col, grid):
        num_rows, num_cols = len(grid), len(grid[0])
        for row_change, col_change in DIRECTIONS:
            neighbor_row, neighbor_col = row + row_change, col + col_change

            if neighbor_row < 0 or neighbor_row >= num_rows:
                continue

            if neighbor_col < 0 or neighbor_col >= num_cols:
                continue

            if grid[neighbor_row][neighbor_col] != 0:
                continue
            yield (neighbor_row, neighbor_col)

    def shortestPathBinaryMatrix(self, grid):
        num_rows, num_cols = len(grid), len(grid[0])

        start_row, start_col = 0, 0
        end_row, end_col = num_rows - 1, num_cols - 1

        if grid[start_row][start_col] != 0 or grid[end_row][end_col] != 0:
            return CANNOT_REACH_END

        queue = deque()
        start_tuple = (start_row, start_col, 1)
        queue.append(start_tuple)

        visited = set()
        visited.add((start_row, start_col))

        while queue:
            row, col, distance_so_far = queue.popleft()

            if row == end_row and col == end_col:
                return distance_so_far

            for neighbor in self.get_neighbors(row, col, grid):
                if neighbor in visited:
                    continue
                neighbor_row, neighbor_col = neighbor
                neighbor_tuple = (neighbor_row, neighbor_col, distance_so_far + 1)
                queue.append(neighbor_tuple)
                visited.add(neighbor)

        return CANNOT_REACH_END
