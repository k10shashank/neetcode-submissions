# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.lowlimit = -1000000000
        self.uplimit = 1000000000
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_node_okay = True

        if root is None:
            return True
        
        if root.left is not None:
            root.left.lowlimit = root.lowlimit
            root.left.uplimit = root.val
            
            if root.left.lowlimit >= root.left.uplimit:
                is_node_okay = False
            elif root.left.val <= root.left.lowlimit:
                is_node_okay = False
            elif root.left.val >= root.left.uplimit:
                is_node_okay = False
        
        if root.right is not None:
            root.right.lowlimit = root.val
            root.right.uplimit = root.uplimit
            
            if root.right.lowlimit >= root.right.uplimit:
                is_node_okay = False
            elif root.right.val <= root.right.lowlimit:
                is_node_okay = False
            elif root.right.val >= root.right.uplimit:
                is_node_okay = False

        return is_node_okay and self.isValidBST(root.left) and self.isValidBST(root.right)
