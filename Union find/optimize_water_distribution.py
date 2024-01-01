from collections import defaultdict
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y: return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True
    

def get_min_cost_to_village_prims(n, wells, pipes):
    adjacency_list = defaultdict(list)

    for house, cost in enumerate(wells):
        adjacency_list[0].append((cost, house + 1))

    for h1, h2, cost in pipes:
        adjacency_list[h1].append((cost, h2))
        adjacency_list[h2].append((cost, h1))

    min_heap = adjacency_list[0]
    heapq.heapify(min_heap)
    visited_set = set([0])

    

    min_cost = 0
    while len(visited_set) < (n + 1):
        cost, node = heapq.heappop(min_heap)
        if node not in visited_set:
            min_cost += cost
            visited_set.add(node)

            for next_cost, next_node in adjacency_list[node]:
                if next_node in visited_set: continue
                heapq.heappush(min_heap, (next_cost, next_node))

    return min_cost

def get_min_cost_to_village_kruskal(n, wells, pipes):
    uf_obj = UnionFind(n + 1)

    ordered_edges = []

    for house, cost in enumerate(wells):
        ordered_edges.append((0, house + 1, cost))

    for house1, house2, cost in pipes:
        ordered_edges.append((house1, house2, cost))

    ordered_edges.sort(key = lambda x: x[2])

    min_cost = 0
    for h1, h2, cost in ordered_edges:
        if uf_obj.union(h1, h2):
            min_cost += cost
    return min_cost

print(get_min_cost_to_village_prims(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]))