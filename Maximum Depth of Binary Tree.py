#Maximum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def rec(root):
            if root:
                return 1 + max(rec(root.left), rec(root.right))
            return 0

        return rec(root)
