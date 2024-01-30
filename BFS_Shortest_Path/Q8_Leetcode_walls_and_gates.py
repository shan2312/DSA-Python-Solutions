from collections import deque

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def get_neighbors(self, row, col, rooms):
        num_rows, num_cols = len(rooms), len(rooms[0])

        for row_change, col_change in DIRECTIONS:
            neighbor_row, neighbor_col = row + row_change, col + col_change

            if neighbor_row < 0 or neighbor_row >= num_rows:
                continue
            if neighbor_col < 0 or neighbor_col >= num_cols:
                continue

            yield (neighbor_row, neighbor_col)

    def update_room_with_distance_to_room(self, queue, visited, rooms):

        while queue:
            row, col, distance_so_far = queue.popleft()

            if rooms[row][col] == -1:
                continue

            rooms[row][col] = distance_so_far

            for neighbor in self.get_neighbors(row, col, rooms):
                if neighbor in visited:
                    continue
                neighbor_row, neighbor_col = neighbor
                neighbor_tuple = (neighbor_row, neighbor_col, distance_so_far + 1)
                queue.append(neighbor_tuple)
                visited.add((neighbor_row, neighbor_col))

    def initialize_queue(self, rooms, queue, visited):
        num_rows, num_cols = len(rooms), len(rooms[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if rooms[row][col] != 0:
                    continue
                start_tuple = (row, col, 0)
                queue.append(start_tuple)
                visited.add((row, col))

    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        visited = set()

        self.initialize_queue(rooms, queue, visited)
        self.update_room_with_distance_to_room(queue, visited, rooms)
