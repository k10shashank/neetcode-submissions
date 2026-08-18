# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    queue = deque()
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is not None:
            self.queue.append([root])
            output.append(root.val)

        while len(self.queue) > 0:
            stage = self.queue.popleft()
            next_stage = []
            next_stage_val = []
            for node in stage:
                if node.left is not None:
                    next_stage.append(node.left)
                    next_stage_val.append(node.left.val)
                if node.right is not None:
                    next_stage.append(node.right)
                    next_stage_val.append(node.right.val)
            if len(next_stage) > 0:
                self.queue.append(next_stage)
                output.append(next_stage_val[-1])

        return output
        