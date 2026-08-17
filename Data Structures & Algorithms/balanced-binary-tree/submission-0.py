# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root)[0]

    def maxDepth(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return (True, 0)
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            isBalanced = leftDepth[0] and rightDepth[0] and abs(leftDepth[1] - rightDepth[1]) <= 1
            maxDepth = 1 + max(leftDepth[1], rightDepth[1])
            return (isBalanced, maxDepth)