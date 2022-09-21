import collections

def get_rainbow(colors):
    d = {'R': 'O', 'O': 'Y', 'Y': 'G', 'G':'B', 'B':'I', 'I':'V'}
    ROWS, COLS = len(colors), len(colors[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visit = set()
    
    def bfs(r, c):
        q = collections.deque([(r, c, 1)])
        visit.add((r, c))
        
        while q:
            r, c, depth = q.popleft()
            if colors[r][c] == 'V':
                return depth
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and (row, col) not in visit and (colors[row][col] == colors[r][c] or colors[row][col] == d[colors[r][c]]):
                    q.append((row, col, depth + 1))
                    visit.add((row, col))
                    
        return float('inf')
    min_length = float('inf')
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visit and colors[r][c] == 'R':
                min_length = min(min_length, bfs(r, c))
                
    
    return min_length if min_length != float('inf') else 0
                
                
if __name__ == '__main__':
    colors = [
        ['R', 'O', 'V', 'V', 'I'],
        ['B', 'I', 'B', 'G', 'Y'],
        ['Y', 'V', 'R', 'O', 'Y'],
        ['B', 'G', 'R', 'Y', 'R']]
    print(get_rainbow(colors))
                
                
                
                
                
                
                
                
                
                
                