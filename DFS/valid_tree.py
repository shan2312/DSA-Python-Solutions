class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.height = [1]*size

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.height[root_x] > self.height[root_y]:
            self.parent[root_y] = root_x

        elif self.height[root_x] < self.height[root_y]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_y] = root_x
            self.height[root_x] += 1
        return True

def is_valid_tree_detect_connection(N, edges):
    if len(edges) != (N - 1):
        return False

    uf_obj = UnionFind(N)

    for node1, node2 in edges:
        uf_obj.union(node1, node2)

    a = set()
    for i in range(N):
        a.add(uf_obj.find(i))

    return len(a) == 1

def is_valid_tree_detect_cycle(N, edges):
    if len(edges) != (N - 1):
        return False

    uf_obj = UnionFind(N)

    for node1, node2 in edges:
        if not uf_obj.union(node1, node2):
            return False
    return True

def build_graph(N, edges):
    adj_list = [[] for _ in range(N)]
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    return adj_list

def is_valid_tree_dfs(N, edges):
    if len(edges) != (N-1):
        return False
    adj_list = build_graph(N, edges)
    seen = set()

    def dfs(root, parent):
        if root in seen and root != parent:
            return

        seen.add(root)

        for neighbor in adj_list[root]:
            if neighbor == parent:
                continue
            dfs(neighbor, root)
    dfs(0, -1)
    return len(seen) == N

print(is_valid_tree_dfs(5, [[0,1], [0, 2], [0, 3], [1, 4]]))

print(is_valid_tree_detect_cycle(5, [[2,3], [1, 2], [1, 3]]))
print(is_valid_tree_detect_connection(5, [[0, 1], [1, 2], [2, 0], [3, 4]]))

    