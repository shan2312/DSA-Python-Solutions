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


def get_smallest_string(s, pairs):
    uf_obj = UnionFind(len(s))

    for index1, index2 in pairs:
        uf_obj.union(index1, index2)

    hashmap = {}

    for index, letter in enumerate(s):
        root = uf_obj.find(index)
        if root not in hashmap:
            hashmap[root] = {'letters': [letter], 'index':[index]}
            continue
        hashmap[root]['letters'].append(letter)
        hashmap[root]['index'].append(index)

    for root in hashmap:
        hashmap[root]['letters'].sort()

    res = ['']*len(s)
    for root, value in hashmap.items():
        for i, index in enumerate(value['index']):
            res[index] = value['letters'][i]

    return ''.join(res)


print(get_smallest_string('dcab', [[0, 3], [1, 2], [0, 2]]))