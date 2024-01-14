from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        parent = root_x
        if root_x == root_y:
            return True, root_x
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            parent = root_y

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return False, parent



def get_min_edges_to_remove(n, edges, k):
    uf_obj = UnionFind(n)
    component_to_edges = defaultdict(defaultdict)

    for node1, node2 in edges:
        is_stale, root = uf_obj.union(node1, node2)
        if root not in component_to_edges:
            component_to_edges[root] = {'count_stale':0, 'other_edges':0}
        if is_stale:
            component_to_edges[root]['count_stale'] += is_stale
            continue
        component_to_edges[root]['other_edges'] += 1

    count_of_components = len(component_to_edges)

    if (k - count_of_components) < 0:
        return -1
    elif (k - count_of_components) == 0:
        return 0
    
    else:
        edges_list = [(k, v['count_stale'], v['other_edges']) for k, v in component_to_edges.items()]
        edges_list.sort(key = lambda x: x[1], reverse=True)

        required_edges = 0
        required_components = (k - count_of_components)
        while required_components > 0 and edges_list:
            component, stale_edges, other_edges = edges_list.pop()
            required_edges += (stale_edges + min(required_components, other_edges))
            required_components -= min(required_components, other_edges)

        if not edges_list:
            return -1
        
        else:
            return required_edges
        

print(get_min_edges_to_remove(10, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [6, 7], [7, 8], [8, 9], [6, 9], [6, 8]], 100))

    

            
