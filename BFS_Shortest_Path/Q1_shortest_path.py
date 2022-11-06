"""
Given an array of edges of an undirected graph and two nodes, return the length of the shortest path between these two nodes. If no such path exists, return -1. Note that the length of a path is the number of edges in the path, not the number of nodes.
"""
from collections import deque, defaultdict

CANNOT_REACH_TARGET = -1


def build_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        node_one, node_two = edge
        graph[node_one].append(node_two)
        graph[node_two].append(node_one)

    return graph


def get_shortest_path_length(edges, start_node, target_node):
    graph = build_graph(edges)

    queue = deque()
    start_node_tuple = (start_node, 0)
    queue.append(start_node_tuple)

    visited = set()
    visited.add(start_node)

    while queue:
        node, distance_so_far = queue.popleft()

        if node == target_node:
            return distance_so_far

        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            neighbor_tuple = (neighbor, distance_so_far + 1)
            queue.append(neighbor_tuple)
            visited.add(neighbor)

    return CANNOT_REACH_TARGET


edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
start_node = "w"
target_node = "z"

print(f"Your answer: {get_shortest_path_length(edges, start_node, target_node)}")
print(f"Correct answer: {2}")
print()
