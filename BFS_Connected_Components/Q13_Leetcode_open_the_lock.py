from collections import deque

COUNT_WHEELS = 4
turn_list = [-1, 1]
num_slots = 10
START_TURNS = 0
CANNOT_REACH_TARGET = -1

class Solution:

    def get_neighbors(self, string):
            for wheel_id in range(self.COUNT_WHEELS):
                wheel_number = int(string[wheel_id])
                
                for delta in self.turn_list:
                    neighboring_wheel_num = (wheel_number + delta) % self.num_slots
                    
                    neighbor_string = string[:wheel_id] + str(neighboring_wheel_num) + string[(wheel_id + 1):]
                    yield neighbor_string
                    
    
    def get_minimum_number_of_turns_from(self, start_string, deadends_set, target):
        queue = deque([(start_string, self.START_TURNS)])
        visited = set()
        visited.add(start_string)

        while queue:
            current_string, current_count_of_turns = queue.popleft()

            if current_string == target:
                return current_count_of_turns
            
            if current_string in deadends_set:
                continue

            for neighbor_string in self.get_neighbors(current_string):
                if neighbor_string in visited:continue
                queue.append((neighbor_string, current_count_of_turns + 1))
                visited.add(neighbor_string)

        return self.CANNOT_REACH_TARGET
    
    def openLock(self, deadends, target):
        deadends_set = set(deadends)
        return self.get_minimum_number_of_turns_from('0000', deadends_set, target)
        
        
        