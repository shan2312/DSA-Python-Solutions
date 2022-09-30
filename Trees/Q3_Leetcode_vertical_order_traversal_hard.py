class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS with vertical order stored. We want sorting by values for same row, col
from collections import deque, defaultdict

def vertical_order_traversal(root):
    queue = deque()
    start_tuple = (root, 0, 0)
    queue.append(start_tuple)

    column_order_hashmap = defaultdict(list)
    mincol = maxcol = 0
    
    while queue:
        curr_node, curr_row_order, curr_column_order = queue.popleft()
        column_order_hashmap[curr_column_order].append((curr_row_order, curr_node.val))
        
        mincol = min(mincol, curr_column_order)
        maxcol = max(maxcol, curr_column_order)

        if curr_node.left:
            left_tuple = (curr_node.left, curr_row_order + 1, curr_column_order - 1)
            queue.append(left_tuple)

        if curr_node.right:
            right_tuple = (curr_node.right, curr_row_order + 1, curr_column_order + 1)
            queue.append(right_tuple)

    column_order_list = []
    for col in range(mincol, maxcol + 1):
        column_order_list.append([value for row, value in sorted(column_order_hashmap[col])])

    return column_order_list

    


    



