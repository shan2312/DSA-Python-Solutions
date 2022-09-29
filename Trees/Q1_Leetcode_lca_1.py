class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

res = []

def find_lowest_common_ancestor(root, p, q):
    if root is None:
        return False
    
    left = find_lowest_common_ancestor(root.left, p, q)
    right = find_lowest_common_ancestor(root.right, p, q)
    mid = 1 if root == p or root == q else 0

    if (left + right + mid) >= 2:
        res.append(root)

    return left or right or mid

