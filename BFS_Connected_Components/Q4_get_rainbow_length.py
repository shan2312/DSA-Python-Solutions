import collections

def get_minimum_rainbow_length(colors):
    rainbow_dict = {'R': 'O', 'O': 'Y', 'Y': 'G', 'G':'B', 'B':'I', 'I':'V'}
    ROWS, COLS = len(colors), len(colors[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seen = set()

    def is_next_in_sequence(current, next):
        current_row, current_col = current[0], current[1]
        next_row, next_col = next[0], next[1]

        is_in_bounds = next_row in range(ROWS) and next_col in range(COLS)
        if not is_in_bounds:
            return False

        is_same_color = colors[next_row][next_col] == colors[current_row][current_col]
        is_next_color = colors[next_row][next_col] == rainbow_dict[colors[current_row][current_col]]
        
        return (is_same_color or is_next_color)

    def get_rainbow_length_from(r, c):
        q = collections.deque([(r, c, 1)])
        seen.add((r, c))
        
        while q:
            r, c, depth = q.popleft()
            if colors[r][c] == 'V':
                return depth
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if  is_next_in_sequence((r, c), (row, col)) and (row, col) not in seen:
                    q.append((row, col, depth + 1))
                    seen.add((row, col))
                    
        return float('inf')

    min_length = float('inf')
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in seen and colors[r][c] == 'R':
                min_length = min(min_length, get_rainbow_length_from(r, c))
                
    
    return min_length if min_length != float('inf') else 0
                
                
if __name__ == '__main__':
    colors = [
        ['R', 'O', 'V', 'V', 'I'],
        ['B', 'I', 'B', 'G', 'Y'],
        ['Y', 'V', 'R', 'O', 'Y'],
        ['B', 'G', 'R', 'Y', 'R']]
    print(get_minimum_rainbow_length(colors))
                
                
                
                
                
                
                
                
                
                
                