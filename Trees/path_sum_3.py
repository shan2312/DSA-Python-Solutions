from collections import defaultdict
from tree import TreeNode

def count_of_path_sum(root, target):
    count = 0
    prefix_sum_dict = defaultdict(int)

    def calculate_prefix_sums(root, current_prefix_sum):
        nonlocal count
        if root is None:
            return

        current_prefix_sum += root.val

        if current_prefix_sum == target:
            count += 1

        if (current_prefix_sum - target) in prefix_sum_dict:
            count += prefix_sum_dict[(current_prefix_sum - target)]

        prefix_sum_dict[current_prefix_sum] += 1
        calculate_prefix_sums(root.left, current_prefix_sum)
        calculate_prefix_sums(root.right, current_prefix_sum)
        prefix_sum_dict[current_prefix_sum] -= 1

    calculate_prefix_sums(root, 0)
    return count


a = TreeNode(3)
b = TreeNode(-2)
c = TreeNode(1)
d = TreeNode(11)

e = TreeNode(val = 3, left=a, right=b)
f = TreeNode(val = 2, right=c)
g = TreeNode(val = 5, left=e, right=f)
h = TreeNode(val = -3, right=d)
i = TreeNode(val = 10, left=g, right=h)

print(count_of_path_sum(i, 8))