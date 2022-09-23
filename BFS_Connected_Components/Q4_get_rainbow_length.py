from collections import deque

RAINBOW_DICT = {'R': 'O', 'O': 'Y', 'Y': 'G', 'G':'B', 'B':'I', 'I':'V'}
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
INITIAL_LENGTH = 1
START_RAINBOW_COLOR, LAST_RAINBOW_COLOR = 'R', 'V'
CANNOT_CREATE_RAINBOW = float('infinity')

def is_in_bounds(colors, row, col):
    num_rows, num_cols = len(colors), len(colors[0])

    is_row_in_bounds = row >= 0 and row < num_rows 
    is_col_in_bounds = col >= 0 and col < num_cols
    is_in_bounds = is_row_in_bounds and is_col_in_bounds

    return is_in_bounds

def is_next_in_sequence(current_color, next_color):
        
        is_same_color = (current_color == next_color)
        is_next_color = (next_color == RAINBOW_DICT[current_color])
        
        return (is_same_color or is_next_color)

def get_rainbow_length_from(start_row, start_col, seen, colors):
    queue = deque([(start_row, start_col, INITIAL_LENGTH)])
    seen.add((start_row, start_col))
    
    while queue:
        current_row, current_col, rainbow_length = queue.popleft()
        
        if colors[current_row][current_col] == LAST_RAINBOW_COLOR:
            return rainbow_length
        
        for delta_row, delta_col in DIRECTIONS:
            next_row, next_col = current_row + delta_row, current_col + delta_col

            if not is_in_bounds(colors, next_row, next_col):continue
            
            current_color, next_color = colors[current_row][current_col], colors[next_row][next_col]
            
            is_in_seen = (next_row, next_col) in seen
            if is_in_seen: continue
            if  not is_next_in_sequence(current_color, next_color): continue
            
            queue.append((next_row, next_col, rainbow_length + 1))
            seen.add((next_row, next_col))
            
    return CANNOT_CREATE_RAINBOW


def get_minimum_rainbow_length(colors):
    num_rows, num_cols = len(colors), len(colors[0])    
    seen = set()

    min_length = CANNOT_CREATE_RAINBOW
    
    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) not in seen and colors[row][col] == START_RAINBOW_COLOR:
                min_length = min(min_length, get_rainbow_length_from(row, col, seen, colors))
                
    
    return 0 if min_length == CANNOT_CREATE_RAINBOW else min_length
                
                
if __name__ == '__main__':
    colors = [
        ['R', 'O', 'V', 'V', 'I'],
        ['B', 'I', 'B', 'G', 'Y'],
        ['Y', 'V', 'R', 'O', 'Y'],
        ['B', 'G', 'R', 'Y', 'R']]
    print(get_minimum_rainbow_length(colors))
                
                
                
                
                
                
                
                
                
                
                