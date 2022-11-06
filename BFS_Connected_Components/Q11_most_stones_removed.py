from collections import deque
import queue


def build_graph(stones):
    adj_list = [[] for _ in range(len(stones))]

    for index1, stone1 in enumerate(stones):
        for index2, stone2 in enumerate(stones):

            if index1 == index2:
                continue
            stone1x, stone1y = stone1[0], stone1[1]
            stone2x, stone2y = stone2[0], stone2[1]

            if stone1x == stone2x or stone1y == stone2y:
                adj_list[index1].append(index2)
                adj_list[index2].append(index1)

    return adj_list


def get_count_of_removable_stones(starting_stone, seen, adj_list):
    queue = deque([starting_stone])
    seen.add(starting_stone)

    count_stones = 0
    while queue:
        current_stone = queue.popleft()
        count_stones += 1

        for next_stone in adj_list[current_stone]:
            if next_stone in seen:
                continue
            queue.append(next_stone)
            seen.add(next_stone)
    count_removable_stones = count_stones - 1
    return count_removable_stones


def get_max_count_of_removable_stones(stones):
    adj_list = build_graph(stones)
    seen = set()

    total_removable_stones_count = 0
    for stone in range(len(stones)):
        if stone in seen:
            continue
        removable_stones_count = get_count_of_removable_stones(stone, seen, adj_list)
        total_removable_stones_count += removable_stones_count

    return total_removable_stones_count


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(get_max_count_of_removable_stones(stones))
