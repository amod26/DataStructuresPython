# Path Sum
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
root
sum
Output will be boolean
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        if not (root.left or root.right) and root.val == sum: return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
