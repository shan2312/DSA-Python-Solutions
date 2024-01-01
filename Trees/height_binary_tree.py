from tree import TreeNode
from collections import deque

def get_height_of_binary_tree_dfs(root):
    if not root:
        return 0
    
    left = get_height_of_binary_tree_dfs(root.left) if root.left else 0
    right = get_height_of_binary_tree_dfs(root.right) if root.right else 0

    return 1 + max(left, right)


def get_height_of_binary_tree_bfs(root):
    queue = deque([root])

    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()

            if current_node.left: queue.append(current_node.left)
            if current_node.right: queue.append(current_node.right)

    return depth


def get_height_of_binary_tree_dfs_iterative(root):
    stack = [(root, 1)]
    max_depth = 0

    while stack:
        current_node, current_depth = stack.pop()
        max_depth = max(max_depth, current_depth)
        if current_node.left: stack.append((current_node.left, current_depth + 1))
        if current_node.right: stack.append((current_node.right, current_depth + 1))

    return max_depth

        



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(get_height_of_binary_tree_dfs_iterative(root))