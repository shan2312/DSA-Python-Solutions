class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# O(N) time and O(1) space
def find_lowest_common_ancestor1(p, q):
    p1, p2 = p, q

    while p1 != p2:
        p1 = p1.parent if p1.parent else q
        p2 = p2.parent if p2.parent else p

    return p1


# O(N) space-time
def find_lowest_common_ancestor2(p, q):
    visited = set()

    while p or q:
        if p in visited:
            return p
        if p:
            visited.add(p)
            p = p.parent

        if q in visited:
            return q
        if q:
            visited.add(q)
            q = q.parent

    return
