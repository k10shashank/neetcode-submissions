# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.maxbefore = None
        self.left = left
        self.right = right

from collections import deque

class Solution:
    queue = deque()
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        if root is not None:
            self.queue.append([root])
            root.maxbefore = -101
            output += 1

        while len(self.queue) > 0:
            stage = self.queue.popleft()
            next_stage = []

            for node in stage:
                if node.left is not None:
                    node.left.maxbefore = max(node.val, node.maxbefore)
                    next_stage.append(node.left)
                    if node.left.val >= node.left.maxbefore:
                        output += 1
                if node.right is not None:
                    node.right.maxbefore = max(node.val, node.maxbefore)
                    next_stage.append(node.right)
                    if node.right.val >= node.right.maxbefore:
                        output += 1
            if len(next_stage) > 0:
                self.queue.append(next_stage)

        return output
        