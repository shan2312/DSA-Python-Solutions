def is_warring_queen(row, col, queens):
    
    for queen_row, queen_col in queens:
        if (row == queen_row) or (col == queen_col) or ((queen_row - queen_col) == (row - col)) or ((queen_row + queen_col) == (row + col)):
            return True
        
    return False 


def solve_queen(N):
    grid = [['.'] * N for _ in range(N)]
    num_rows, num_cols = len(grid), len(grid[0])

    def solve_queen_for(N, queens):
        if N == 0:
            return True
        
        for r in range(num_rows):
            for c in range(num_cols):
                if  is_warring_queen(r, c, queens):
                   continue

                grid[r][c] = 'Q'
                queens.append((r, c))
                if solve_queen_for(N - 1, queens):
                    return True
                
                grid[r][c] = '.'
                queens.pop()

        return False
    
    solve_queen_for(N, [])
    return grid


print(solve_queen(5))


