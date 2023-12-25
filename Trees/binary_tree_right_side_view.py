from collections import deque
from tree import TreeNode

def get_right_side_view(root):
    right_view_list = []
    q = deque([root])

    if root is None:
        return right_view_list

    while q:
        for _ in range(len(q)):
            current_node = q.popleft()

            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)

        right_view_list.append(current_node.val)

    return right_view_list
    

a = TreeNode(val = 2, left = None, right = None)
b = TreeNode(val = 1, left = None, right = a)
c = TreeNode(val = 4, left = None, right=None)
d = TreeNode(val = 3, left=b, right=c)
print(get_right_side_view(d))
