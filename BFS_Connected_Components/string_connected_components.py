class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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


def is_strings_similar(string1, string2):
    if string1 == string2: return True 
    count = 0
    for index in range(len(string1)):
        if string1[index] == string2[index]: continue
        
        count += 1
        
    return count == 2
    
def get_connected_groups(strings):
    uf_obj = UnionFind(len(strings))
    comp = len(strings)
    for index1, string1 in enumerate(strings):
        for index2, string2 in enumerate(strings):
            if not is_strings_similar(string1, string2) or index1 == index2: continue
            if not uf_obj.union(index1, index2): continue
            comp -= 1
            
    return comp



print(get_connected_groups(['rats', 'tars', 'tars', 'astr', 'satr']))
