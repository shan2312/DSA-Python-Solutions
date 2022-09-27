from collections import deque
DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

class Solution:
    def get_neighbors(self, row, col, mat):
        num_rows, num_cols = len(mat), len(mat[0])
        
        for row_change, col_change in DIRECTIONS:
            neighbor_row, neighbor_col = row + row_change, col + col_change
            
            if neighbor_row < 0 or neighbor_row >= num_rows: continue
            if neighbor_col < 0 or neighbor_col >= num_cols: continue
                
            yield (neighbor_row, neighbor_col)
            
    def update_distance_from_zero_for_all_cells(self, mat, queue, visited):
        
        while queue:
            row, col, distance_so_far = queue.popleft()
            
            for neighbor in self.get_neighbors(row, col, mat):

                if neighbor in visited: continue
                neighbor_row, neighbor_col = neighbor
                neighbor_tuple = (neighbor_row, neighbor_col, distance_so_far + 1)
                queue.append(neighbor_tuple)
                visited.add(neighbor)
                mat[neighbor_row][neighbor_col] = distance_so_far + 1
    
    def initialize_queue(self, mat, queue, visited):
        num_rows, num_cols = len(mat), len(mat[0])
        
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] != 0: continue
                start_tuple = (row, col, 0)
                queue.append(start_tuple)
                visited.add((row, col))
            
        
    def updateMatrix(self, mat):
        queue = deque()
        visited = set()
        
        self.initialize_queue(mat, queue, visited)
        self.update_distance_from_zero_for_all_cells(mat, queue, visited)
        return mat