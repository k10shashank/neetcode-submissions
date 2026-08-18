# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    arr = []
    cnt = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.cnt = 0
        self.inOrder(root)
        return self.arr[k-1]
    
    def inOrder(self, root: Optional[TreeNode]):
        if root is not None:
            if root.left is not None:
                self.inOrder(root.left)
            
            self.arr.append(root.val)
            self.cnt += 1

            if root.right is not None:
                self.inOrder(root.right)
        