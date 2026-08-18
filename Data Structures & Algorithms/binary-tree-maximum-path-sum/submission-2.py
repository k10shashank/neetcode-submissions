# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    MAXX = -30000000

    def maxSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftSum = self.maxSum(root.left)
            rightSum = self.maxSum(root.right)
            self.MAXX = max(self.MAXX, max(leftSum, 0) + max(rightSum, 0) + root.val)
            return root.val + max(leftSum, rightSum, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum(root)
        return self.MAXX
        