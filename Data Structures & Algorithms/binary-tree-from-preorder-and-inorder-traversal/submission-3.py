# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    preorderIdx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderHash = {val: idx for idx, val in enumerate(inorder)}

        def func(l, r):
            if l > r:
                return None
            node = TreeNode(preorder[self.preorderIdx])
            mid = inorderHash[preorder[self.preorderIdx]]
            self.preorderIdx += 1

            node.left = func(l, mid - 1)
            node.right = func(mid + 1, r)

            return node
        
        return func(0, len(inorder) - 1)
