from collections import deque


def build_graph(grid):
    count_of_friends = len(grid)
    adj_list = [[] for i in range(count_of_friends)]

    for friend1_id in range(count_of_friends):
        for friend2_id in range(count_of_friends):

            is_upper_diagonal = friend1_id >= friend2_id
            is_not_friends = grid[friend1_id][friend2_id] != 1

            if is_upper_diagonal or is_not_friends:
                continue

            adj_list[friend1_id].append(friend2_id)
            adj_list[friend2_id].append(friend1_id)

    return adj_list


def mark_friend_circle_as_visited(start_friend_id, seen, adj_list, grid):
    queue = deque([start_friend_id])
    seen.add(start_friend_id)

    while queue:
        current_friend_id = queue.popleft()

        for next_friend_id in adj_list[current_friend_id]:
            if next_friend_id not in seen:
                queue.append(next_friend_id)
                seen.add(next_friend_id)


def get_friend_circles_count(grid):
    count_of_friends = len(grid)
    seen = set()
    adj_list = build_graph(grid)

    count_of_friend_circles = 0

    for friend_id in range(count_of_friends):
        if friend_id not in seen:
            mark_friend_circle_as_visited(friend_id, seen, adj_list, grid)
            count_of_friend_circles += 1

    return count_of_friend_circles


if __name__ == "__main__":
    grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(get_friend_circles_count(grid))
