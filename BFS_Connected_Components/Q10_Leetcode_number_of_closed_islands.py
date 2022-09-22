import collections
def closedIsland(grid):
    ROWS, COLS = len(grid), len(grid[0])
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seen = set()
    

    def is_closed_island(r, c):
        q = collections.deque([(r, c)])
        seen.add((r, c))
        closed = True
        while q:
            row, col = q.popleft()
            is_boundary = row == ROWS - 1 or row == 0 or col == 0 or col == COLS - 1
            if is_boundary:
                    closed = False
            for dr, dc in directions:
                r, c = row + dr, col + dc
                is_in_bounds = r in range(ROWS) and c in range(COLS)
                is_not_in_seen = (r, c) not in seen
                if is_in_bounds and is_not_in_seen and grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))
        return closed
    
    count_closed = 0
                    
    for r in range(ROWS):
        for c in range(COLS):
            is_not_boundary = r != 0 and r != ROWS - 1 and c != 0 and c != COLS - 1
            if grid[r][c] == 0 and (r, c) not in seen and is_not_boundary:
                count_closed += is_closed_island(r, c)
                
    return count_closed
                
                    
                