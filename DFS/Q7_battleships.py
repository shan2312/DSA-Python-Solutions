EMPTY = '.'

class Solution:
    def __init__(self) -> None:
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


    def is_in_bounds(self, row, col, board):
        num_rows, num_cols = len(board), len(board[0])

        is_row_in_bounds = row >=0 and row < num_rows
        is_col_in_bounds = col >=0 and col < num_cols

        is_in_bounds = is_row_in_bounds and is_col_in_bounds
        return is_in_bounds


    def mark_battleship_as_visited(self, board, start_cell, visited):
        
        start_row, start_col = start_cell

        if (start_row, start_col) in visited or board[start_row][start_col] == '.':
            return

        visited.add(start_cell)

        for delta_row, delta_col in self.directions:
            neighbor_row = start_row + delta_row
            neighbor_col = start_col + delta_col


            if not self.is_in_bounds(neighbor_row, neighbor_col, board):
                continue

            if board[neighbor_row][neighbor_col] == EMPTY:
                continue

            neighbor_tuple = (neighbor_row, neighbor_col)
            self.mark_battleship_as_visited(board, neighbor_tuple, visited)


    def countBattleships(self, board):
        num_rows, num_cols = len(board), len(board[0])
        visited = set()
        count_of_battleships = 0

        for row in range(num_rows):
            for col in range(num_cols):
                curr_tuple =  (row, col)
                if curr_tuple in visited or board[row][col] == EMPTY:
                    continue
                self.mark_battleship_as_visited(board, curr_tuple, visited)
                count_of_battleships += 1

        return count_of_battleships





