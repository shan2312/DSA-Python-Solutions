class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


res = []


def find_lowest_common_ancestor(root, p, q):
    if root.val > max(p.val, q.val):
        return find_lowest_common_ancestor(root.left, p, q)
    elif root.val < min(p.val, q.val):
        return find_lowest_common_ancestor(root.right, p, q)
    else:
        return root