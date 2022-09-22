import collections
def maxAreaOfIsland(grid):
    ROWS, COLS = len(grid), len(grid[0])
    
    seen = set()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def get_island_area(r, c):
        q = collections.deque([(r, c)])
        seen.add((r, c))
        count = 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                is_in_bounds = row in range(ROWS) and col in range(COLS)
                is_not_in_seen = (row, col) not in seen
                if is_not_in_seen and is_in_bounds and grid[row][col] == 1:
                    q.append((row, col))
                    seen.add((row, col))
            count += 1
        return count
    
    max_count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in seen:
                max_count = max(max_count, get_island_area(r, c))
                
    return max_count