# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    MAXX = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.MAXX

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            self.MAXX = max(self.MAXX, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        