DIRECTIONS = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
from collections import deque

class Solution:
    
    def get_neighbors(self, x, y):
        
        for x_change, y_change in DIRECTIONS:
            neighbor_x, neighbor_y = x + x_change, y + y_change
            
            yield (neighbor_x, neighbor_y)
            
            
    def add_neighbors_to_queue(self, x, y, queue, visited_hashmap, num_moves):
        for neighbor in self.get_neighbors(x, y):
                if neighbor in visited_hashmap: continue
                neighbor_x, neighbor_y = neighbor
                
                neighbor_tuple = (neighbor_x, neighbor_y, num_moves + 1)
                queue.append(neighbor_tuple)
                visited_hashmap[(neighbor_x, neighbor_y)] = num_moves + 1
    
    def minKnightMoves(self, x: int, y: int) -> int:
        
        origin_queue = deque()
        start_tuple = (0, 0, 0)
        origin_queue.append(start_tuple)
        
        target_queue = deque()
        target_tuple = (x, y, 0)
        target_queue.append(target_tuple)
        
        
        origin_visited_hashmap = {(0, 0): 0}
        target_visited_hashmap = {(x, y): 0}
        
        while True:
            curr_origin_x, curr_origin_y, num_moves_so_far_from_origin = origin_queue.popleft()
            curr_target_x, curr_target_y, num_moves_so_far_from_target = target_queue.popleft()
            
            if (curr_origin_x, curr_origin_y) in target_visited_hashmap:
                return num_moves_so_far_from_origin + target_visited_hashmap[(curr_origin_x, curr_origin_y)]
            
            if (curr_target_x, curr_target_y) in origin_visited_hashmap:
                return num_moves_so_far_from_target + origin_visited_hashmap[(curr_target_x, curr_target_y)]
            
            
            self.add_neighbors_to_queue(curr_origin_x, curr_origin_y, origin_queue, origin_visited_hashmap, num_moves_so_far_from_origin)
            
            self.add_neighbors_to_queue(curr_target_x, curr_target_y, target_queue, target_visited_hashmap, num_moves_so_far_from_target)
            