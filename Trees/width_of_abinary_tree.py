from tree import TreeNode
from typing import Optional

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        max_width = 0

        while queue:
            min_index = float('inf')
            max_index = -1 * float('inf')

            for _ in range(len(queue)):
                node, index = queue.popleft()
                min_index = min(min_index, index)
                max_index = max(max_index, index)

                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index + 1))

            
            max_width = max(max_width, max_index - min_index + 1)

        return max_width
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1, 1)])

        prev_num = prev_level = max_width = 0

        while queue:
            node, num, level = queue.popleft()

            if prev_level < level:
                prev_num = num
                prev_level = level

            max_width = max(max_width, num - prev_num + 1)

            if node.left:
                queue.append((node.left, 2*num, level + 1))

            if node.right:
                queue.append((node.right, 2*num + 1, level + 1))

        return max_width
        # queue = deque([(root, 1)])
        # max_width = 0

        # while queue:
        #     min_index = float('inf')
        #     max_index = -1 * float('inf')

        #     for _ in range(len(queue)):
        #         node, index = queue.popleft()
        #         min_index = min(min_index, index)
        #         max_index = max(max_index, index)

        #         if node.left:
        #             queue.append((node.left, 2*index))
        #         if node.right:
        #             queue.append((node.right, 2*index + 1))

            
        #     max_width = max(max_width, max_index - min_index + 1)

        # return max_width
