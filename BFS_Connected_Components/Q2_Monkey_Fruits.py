import math
from collections import deque


def build_graph(trees):
    adj_list = [[] for _ in range(len(trees))]

    for tree1_id, tree1 in enumerate(trees):
        for tree2_id, tree2 in enumerate(trees):
            if tree1_id == tree2_id:
                continue

            x_one, y_one, num_fruits_one, vine_length_one = tree1
            x_two, y_two, num_fruits_two, vine_length_two = tree2

            distance = math.sqrt((x_one - x_two) ** 2 + (y_one - y_two) ** 2)

            if vine_length_one < distance or vine_length_two < distance:
                continue
            adj_list[tree1_id].append(tree2_id)
            adj_list[tree2_id].append(tree1_id)

    return adj_list


def get_max_reachable_fruits_from(start_tree_id, seen, adj_list):
    start_tree_fruits = trees[start_tree_id][2]
    queue = deque([(start_tree_id, start_tree_fruits)])
    seen.add(start_tree_id)

    total_fruits = 0

    while queue:
        current_tree_id, current_tree_fruits = queue.popleft()
        total_fruits += current_tree_fruits

        for next_tree_id in adj_list[current_tree_id]:
            if next_tree_id in seen:
                continue

            next_tree_fruits = trees[next_tree_id][2]
            queue.append((next_tree_id, next_tree_fruits))
            seen.add(next_tree_id)

    return total_fruits


def get_max_fruits(trees):
    adj_list = build_graph(trees)
    seen = set()

    max_reachable_fruits = 0

    for tree_id in range(len(trees)):
        if tree_id in seen:
            continue
        max_reachable_fruits_from = get_max_reachable_fruits_from(
            tree_id, seen, adj_list
        )
        max_reachable_fruits = max(max_reachable_fruits, max_reachable_fruits_from)

    return max_reachable_fruits


if __name__ == "__main__":
    trees = [[2, 4, 2, 6], [10, 4, 5, 5], [3, 8, 3, 6], [12, 8, 6, 5], [1, 6, 2, 6]]
    print(get_max_fruits(trees))
