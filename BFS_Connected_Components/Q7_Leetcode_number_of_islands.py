import collections

def numIslands(grid):
    if not grid:
        return 0

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ROWS, COLS = len(grid), len(grid[0])

    seen = set()
    num_islands = 0
    
    def traverse_island(r,c):
        q = collections.deque([(r, c)])
        seen.add((r, c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                is_in_bounds = row in range(ROWS) and col in range(COLS)
                is_not_in_seen = (row, col) not in seen
                if is_in_bounds and grid[row][col] == "1" and is_not_in_seen:
                    q.append((row, col))
                    seen.add((row, col))
    
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in seen or grid[r][c] != "1":continue
            traverse_island(r, c)
            num_islands += 1
                    
    return num_islands
