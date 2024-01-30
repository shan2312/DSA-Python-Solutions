
from collections import defaultdict

def build_graph(equations, values):
    adjacency_list = defaultdict(list)

    for (node1, node2), value in zip(equations, values):
        adjacency_list[node1].append((node2, value))
        adjacency_list[node2].append((node1, 1/value))

    return adjacency_list

def dfs(source, target, adjacency_list, visited_set, current_product):
    if source == target:
        return current_product
    
    visited_set.add(source)

    for neighbor, prod in adjacency_list[source]:
        if neighbor in visited_set: continue

        next_product = dfs(neighbor, target, adjacency_list, visited_set, current_product * prod)
        if next_product != -1:
            return next_product
        
    visited_set.remove(source)

    return -1





def evaluate_divisions(equations, values, queries):
    adjacency_list = build_graph(equations, values)

    result = []
    for node1, node2 in queries:
        visited_set = set()
        if node1 not in adjacency_list:
            result.append(-1)
            continue
        result.append(dfs(node1, node2, adjacency_list, visited_set, 1))

    return result



print(evaluate_divisions([['a', 'b'], ['b', 'c'], ['c', 'e']], [2, 4, 5], [['a', 'e'], ['e', 'a'], ['b', 'b'], ['z', 'z']]))