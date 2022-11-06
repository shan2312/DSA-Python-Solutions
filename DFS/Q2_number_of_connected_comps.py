
from collections import defaultdict

class ComponentsInGraph:
    def __init__(self) -> None:
        pass

    def build_graph(self, edges):
        adjacency_list = defaultdict(list)
        
        for ancestor_node, descendant_node in edges:
            adjacency_list[ancestor_node].append(descendant_node)
            adjacency_list[descendant_node].append(ancestor_node)

        return adjacency_list

    def mark_component_as_visited(self, start_node, adjacency_list, visited_set):
        if start_node in visited_set:
            return

        visited_set.add(start_node)

        for neighbor in adjacency_list[start_node]:
            self.mark_component_as_visited(neighbor, adjacency_list, visited_set)

    def count_components(self, edges):

        adjacency_list = self.build_graph(edges)
        visited_set = set()
        count_of_components = 0

        for start_node in range(n):
            if start_node in visited_set: continue
            self.mark_component_as_visited(start_node, adjacency_list, visited_set)
            count_of_components += 1

        return count_of_components