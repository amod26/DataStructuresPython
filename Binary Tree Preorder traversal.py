# Binary Tree Preorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        value = []

        def collect(root):
            if root:
               # First print the data of node
                value.append(root.val)

                # Then recur on left child
                collect(root.left)

                # Finally recur on right child
                collect(root.right)
        collect(root)
        return value

# One line Code

# return [root.val]+ self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
