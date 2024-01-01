from tree import TreeNode

# TC: O(N), SC: O(N)
def get_kth_smallest_element_recursive(root, k): 
    inorder_list = []

    def inorder_traversal(root):
        if root is None:
            return

        inorder_traversal(root.left)
        inorder_list.append(root.val)
        inorder_traversal(root.right)

    inorder_traversal(root)
    return inorder_list[k - 1]

# TC: O(H + K), SC: O(H)
def get_kth_smallest_element_iterative(root, k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        k -= 1

        if k == 0:
            return root.val

        root = root.right


a = TreeNode(val = 1, left = None, right = None)
b = TreeNode(val = 2, left = a, right = None)
c = TreeNode(val = 4, left = None, right=None)
d = TreeNode(val = 3, left = b, right=c)
e = TreeNode(val = 6, left = None, right = None)
f = TreeNode(val = 5, left = d, right = e)

print(get_kth_smallest_element_recursive(f, 3))    