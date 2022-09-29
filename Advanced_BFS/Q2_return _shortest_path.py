"""
Let’s set up a simple problem so that we can concretely study this strategy. Suppose we’re given 3 inputs:
A start city, e.g. 5
An end city, e.g. 10
A list of roads, e.g. [[5,7], [5,3], [7,6], [7,4], [3,9], [6,4], [4,10], [4,9]]
and we’re asked to return the shortest path (as an array) from the start city to the end city.
"""

from collections import defaultdict, deque
NO_VALID_PATH = []

def build_graph(edges):
    graph = defaultdict(list)
    
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph

def construct_path(start_city, end_city, ideal_prev_city_map):
    curr_city = end_city
    path = []
    
    while curr_city:
        path.append(curr_city)
        curr_city = ideal_prev_city_map[curr_city]

    path.reverse()
    return path

def get_shortest_path(start_city, end_city, roads):

    graph = build_graph(roads)

    ideal_prev_city_map = {}
    queue = deque()
    start_tuple = (start_city, None)
    queue.append(start_tuple)

    visited = set()
    visited.add(start_city)

    while queue:
        curr_city, prev_city = queue.popleft()

        if curr_city not in ideal_prev_city_map:
            ideal_prev_city_map[curr_city] = prev_city

        for neighbor in graph[curr_city]:
            if neighbor in visited:
                continue
            neighbor_tuple = (neighbor, curr_city)
            queue.append(neighbor_tuple)
            visited.add(neighbor)

    if end_city not in ideal_prev_city_map:
        return NO_VALID_PATH
        
    return construct_path(start_city, end_city, ideal_prev_city_map)


if __name__ == '__main__':
    roads = [[5,7], [5,3], [7,6], [7,4], [3,9], [6,4], [4,10], [4,9]]
    print(get_shortest_path(5, 9, roads))
