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

        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True



def is_graph_valid_tree(edges, n):
    if len(edges) != (n - 1):
        return False
    
    uf_obj = UnionFind(n)

    for node1, node2 in edges:
        if not uf_obj.union(node1, node2):
            return False
        
    return True


print(is_graph_valid_tree([[0,1], [1,2], [2,3], [1,3], [1,4]], 5))
