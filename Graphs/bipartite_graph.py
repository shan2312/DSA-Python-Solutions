from collections import defaultdict 

from enum import Enum

# class syntax
class Color(Enum):
    UNCOLORED = -1
    RED = 1
    GREEN = 2

class Solution:
    def is_color_safe(self, node, color, color_map, adj_list):
        for neighbor in adj_list[node]:
            if color_map[neighbor] == color: return False
            
        return True

    def isBipartite(self, graph) -> bool:
        color_map = {node: Color.UNCOLORED for node in range(len(graph))}

        def traverse_graph(start_node, V, adj, color_map):
            if color_map[start_node] != Color.UNCOLORED:
                return True

            for color in Color:
                if color == Color.UNCOLORED: continue
                if not self.is_color_safe(start_node, color, color_map, adj):
                    continue
	            
                color_map[start_node] = color
                
                is_neighbors_colored = True
                for neighbor in adj[start_node]:
                    if color_map[neighbor] != Color.UNCOLORED: continue
                    print(neighbor)
                    is_neighbors_colored &= traverse_graph(neighbor, V, adj, color_map)
                    if not is_neighbors_colored: break
                
                else:
                    return True
            

            color_map[start_node] = Color.UNCOLORED
            return False
        

        for node in range(len(graph)):
            if not traverse_graph(node, len(graph), graph, color_map):
                return False
        
        return True
	    