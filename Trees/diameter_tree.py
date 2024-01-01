from tree import TreeNode

def get_diameter_of_binary_tree(root):
    def get_max_path(root):
        left = get_max_path(root.left) if root.left else (-1, -1)
        right = get_max_path(root.right) if root.right else (-1, -1)

        return max(left[0] + 1, right[0] + 1), max(left[1], right[1], (left[0] + right[0] + 2))
    

    return get_max_path(root)[1]


a = TreeNode(val=4)
b = TreeNode(val=5)
c = TreeNode(val=3)
d = TreeNode(val=2, left = a, right = b)
e = TreeNode(val=1, left = d, right = c)

print(get_diameter_of_binary_tree(e))