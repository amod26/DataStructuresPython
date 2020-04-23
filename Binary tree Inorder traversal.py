# binary tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def collect(root):
            if root:
                collect(root.left)
                l.append(root.val)
                collect(root.right)
        collect(root)
        return l
