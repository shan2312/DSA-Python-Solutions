import collections

def floodFill(self, image, sr, sc, color):
    """
    BFS traversal on the grid. Add visited cells to set and color all visited cells in the end
    """

    ROWS, COLS = len(image), len(image[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    q = collections.deque([(sr, sc)])
    seen = set()
    seen.add((sr, sc))
    
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and (row, col) not in seen and image[row][col] == image[r][c]:
                    q.append((row, col))
                    seen.add((row, col))
                    
    for r, c in list(seen):
        image[r][c] = color
        
    return image
                
        
        