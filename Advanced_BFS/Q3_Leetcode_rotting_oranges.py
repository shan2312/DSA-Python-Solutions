from collections import deque

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def initialize_queue_with_rotten_oranges(self, grid, queue, visited):
        num_rows, num_cols = len(grid), len(grid[0])
        fresh = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))

                fresh += 1 if grid[row][col] == 1 else 0

        return fresh

    def get_neighbors(self, row, col, grid):
        num_rows, num_cols = len(grid), len(grid[0])

        for row_change, col_change in DIRECTIONS:
            neighbor_row, neighbor_col = row + row_change, col + col_change

            if neighbor_row < 0 or neighbor_row >= num_rows:
                continue
            if neighbor_col < 0 or neighbor_col >= num_cols:
                continue

            yield (neighbor_row, neighbor_col)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        count_fresh_oranges = self.initialize_queue_with_rotten_oranges(
            grid, queue, visited
        )

        minimum_time = 0
        while queue:
            for i in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                for neighbor in self.get_neighbors(curr_row, curr_col, grid):
                    neighbor_row, neighbor_col = neighbor

                    if neighbor in visited:
                        continue
                    if grid[neighbor_row][neighbor_col] != 1:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
                    count_fresh_oranges -= 1
            minimum_time += 1

        if minimum_time > 0:
            minimum_time = minimum_time - 1

        return minimum_time if count_fresh_oranges == 0 else -1


#         rows, cols = len(grid), len(grid[0])
#         time = fresh = 0
#         q = collections.deque()

#         for r in range(rows):
#             for c in range(cols):
#                 if(grid[r][c]==2):
#                     q.append((r,c))
#                 elif(grid[r][c]==1):
#                     fresh+=1

#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         while q and fresh>0:
#             for i in range(len(q)):
#                 row,col = q.popleft()
#                 for dr, dc in directions:
#                     r,c = row+dr, col+dc
#                     if(r in range(rows) and
#                       c in range(cols) and
#                       grid[r][c]==1):
#                         grid[r][c]=2
#                         q.append((r,c))
#                         fresh-=1
#             time+=1
#             print(time)
#         return time if fresh==0 else -1
