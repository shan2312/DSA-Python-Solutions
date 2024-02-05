from collections import defaultdict, deque

def build_graph(edges, n):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for node1, node2 in edges:
        graph[node1].append(node2)
        indegree[node2] += 1

    for node in range(n):
        if node not in graph:
            graph[node] = []
        if node not in indegree:
            indegree[node] = 0

    return graph, indegree

def get_largest_path_value_dfs_solve(edges, nodes_str):
    n = len(nodes_str)
    paths = [[0 for i in range(26)] for _ in range(n)]
    graph, indegre = build_graph(edges, n)

    def update_path(nodes_str, neighbor, paths, start):
        if start == -1: 
            for i in range(26):
                paths[neighbor][i] = max(paths[neighbor][i], (ord(nodes_str[neighbor]) - ord('A'))== i)
            return paths
        for i in range(26):
            paths[neighbor][i] = max(paths[neighbor][i], paths[start][i] + (i == (ord(nodes_str[neighbor]) - ord('A'))))

        return paths
    
    def get_larget_path_value_dfs(start, visited, nodes_str, graph, paths, cycle_set, parent):
        if start in cycle_set:
            return False
        
        if start in visited:
            return True
        
        visited.add(start)
        cycle_set.add(start)
        update_path(nodes_str, start, paths, parent)

        for neighbor in graph[start]:
            if not get_larget_path_value_dfs(neighbor, visited, nodes_str, graph, paths, cycle_set, start):
                return False

        cycle_set.remove(start)
        return True

    visited = set()
    cycle_set = set()

    for node in range(n):
        if not get_larget_path_value_dfs(node, visited, nodes_str, graph, paths, cycle_set, -1):
            return -1
        
    return max([i for p in paths for i in p])



def get_largest_path_value(edges, nodes_str):
    n = len(nodes_str)
    graph, indegree = build_graph(edges, n)

    zero_indegree_queue = deque([k for k in range(n) if indegree[k] == 0])

    paths = [[0 for i in range(26)] for _ in range(n)]

    for k in range(n):
        if indegree[k] != 0: continue
        paths[k][ord(nodes_str[k]) - ord('A')] += 1

    while zero_indegree_queue:
        current_node = zero_indegree_queue.popleft()

        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1

            for i in range(26):
                paths[neighbor][i] = max(paths[neighbor][i], paths[current_node][i] + (i == ord(nodes_str[neighbor]) - ord('A')))

            if indegree[neighbor] == 0:
                zero_indegree_queue.append(neighbor)

    return max([alphabet_count for value in paths for alphabet_count in value]) if sum(indegree.values()) == 0 else -1




def get_largest_path_value_binary_search(edges, nodes_str):
    graph, indegree = build_graph(edges, len(nodes_str))

    min_path_value, max_path_value = 0, len(nodes_str)

    while min_path_value <= max_path_value:
        middle_path_value = (min_path_value + max_path_value)//2

        is_valid = 
        if 

print(get_largest_path_value([(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)], 'ABACA'))

print(get_largest_path_value_dfs_solve([(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)], 'ABACA'))


print(get_largest_path_value([(0, 0)], 'A'))
print(get_largest_path_value_dfs_solve([(0, 0)], 'A'))

edges = [(0, 1), (0, 6), (1, 2), (1, 4), (2, 3), (4, 5)]
n = 7
print(get_largest_path_value(edges, 'ABBADAA'))
print(get_largest_path_value_dfs_solve(edges, 'ABBADAA'))



