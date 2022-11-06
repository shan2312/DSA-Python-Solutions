# Battleships on a board
# Each battleship size is 1:n
# We have to determine count of battleships

# board a matrix of m * n, a battleship will be occupying cells on the board
"""
11110000
00000000
10101111
10100000
00000111

5 battleships
"""

from enum import Enum
import heapq
from collections import deque

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
BATTLESHIP = 1


class BattleShipAlignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class BattleShip:
    def __init__(
        self, size=0, coordinates=(0, 0), direction=BattleShipAlignment.HORIZONTAL
    ):
        self.size = size
        self.coordinates = coordinates
        self.direction = direction

    def print_battleship(self):
        print(
            "Battleship size {}, coordinates {}, Alignment {}".format(
                self.size, self.coordinates, self.direction.name
            )
        )


def get_neighbors(row, col, board):
    num_rows, num_cols = len(board), len(board[0])

    for row_change, col_change in DIRECTIONS:
        neighbor_row, neighbor_col = row + row_change, col + col_change

        if neighbor_row < 0 or neighbor_row >= num_rows:
            continue
        if neighbor_col < 0 or neighbor_col >= num_cols:
            continue

        yield (neighbor_row, neighbor_col)


def mark_battleship_as_visited(board, start_row, start_col, visited):
    queue = deque()
    start_tuple = (start_row, start_col)
    queue.append(start_tuple)

    visited.add(start_tuple)

    battle_ship = BattleShip()
    battle_ship.coordinates = start_tuple

    while queue:
        curr_row, curr_col = queue.popleft()
        last_row = curr_row
        battle_ship.size += 1
        neighbors = get_neighbors(curr_row, curr_col, board)

        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor

            if neighbor in visited:
                continue
            if board[neighbor_row][neighbor_col] != BATTLESHIP:
                continue

            queue.append(neighbor)
            visited.add(neighbor)

    battle_ship.direction = (
        BattleShipAlignment.HORIZONTAL
        if last_row == start_row
        else BattleShipAlignment.VERTICAL
    )
    return battle_ship


def get_battleship_counts(board, k):

    num_rows, num_cols = len(board), len(board[0])
    visited = set()
    count_battleships = 0
    battleships_dict = {}

    max_heap = []
    heapq.heapify(max_heap)

    for row in range(num_rows):
        for col in range(num_cols):

            if (row, col) in visited:
                continue
            if board[row][col] != BATTLESHIP:
                continue

            curr_battle_ship = mark_battleship_as_visited(board, row, col, visited)
            battleships_dict[(row, col)] = curr_battle_ship

            if len(max_heap) < k:
                heapq.heappush(max_heap, [-1 * curr_battle_ship.size, (row, col)])
            elif len(max_heap) == k and max_heap[0][0] < -1 * curr_battle_ship.size:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, [-1 * curr_battle_ship.size, (row, col)])

            count_battleships += 1

    k_smallest_battleships = []

    for _, location in max_heap:
        k_smallest_battleships.append(battleships_dict[location])

    return count_battleships, k_smallest_battleships


if __name__ == "__main__":
    board = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1],
    ]
    count, bs = get_battleship_counts(board, 4)

    for index, b in enumerate(bs):
        b.print_battleship()

# maxHeap size k
# [3,4,5]
"""
11110000
00000000
10101111
10100000
00000111
01234567
5 * 8
visited = set((0, 0), (0, 1), (0, 2), (0, 3))
q = []
count = 5

Time - M -> rows, N -> cols, O(M * N) -> O(M*N*logK)
Space - O(M*N + k) -> 

(start_index, size, direction) - ((0,0), 5, 'HORIZONTAL')
(start_index, end_index)
"""
