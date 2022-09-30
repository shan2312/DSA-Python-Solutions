class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque, defaultdict

def vertical_order_traversal(root):

    if not root:
        return []

    queue = deque()
    start_tuple = (root, 0)
    queue.append(start_tuple)

    min_col = max_col = 0
    vertical_order_hashmap = defaultdict(list)

    while queue:
        curr_node, curr_column_order = queue.popleft()
        
        vertical_order_hashmap[curr_column_order].append(curr_node.val)
        
        min_col = min(min_col, curr_column_order)
        max_col = max(max_col, curr_column_order)

        if curr_node.left:
            left_tuple = (curr_node.left, curr_column_order - 1)
            queue.append(left_tuple)

        if curr_node.right:
            right_tuple = (curr_node.right, curr_column_order + 1)
            queue.append(right_tuple)

    vertical_order_list = []
    for col in range(min_col, max_col + 1):
        vertical_order_list.append(vertical_order_hashmap[col])

    return vertical_order_list
