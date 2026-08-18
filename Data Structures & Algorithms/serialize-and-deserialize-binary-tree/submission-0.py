# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''

        q = deque()
        q.append(root)
        output = []
        while len(q) > 0:
            node = q.popleft()
            if node is None:
                output.append(None)
            else:
                output.append(node.val)
                q.append(node.left)
                q.append(node.right)

        output_str = ''
        trailing_null = True
        for i in range(len(output)-1,-1,-1):
            if output[i] is None:
                if trailing_null:
                    continue
                else:
                    output_str = 'null,' + output_str
            else:
                if trailing_null:
                    output_str = str(output[i])
                    trailing_null = False
                else:
                    output_str = f'{output[i]},{output_str}'
        return output_str

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        if len(arr) == 0:
            return None
        
        for i in range(len(arr)):
            if arr[i] == 'null':
                arr[i] = None
            else:
                arr[i] = TreeNode(arr[i])

        null_count = 0
        N = len(arr)
        for i in range(N):
            print(i)
            if arr[i] is None:
                null_count += 1
            else:
                left_idx = i * 2 + 1 - null_count * 2
                right_idx = left_idx + 1
                if left_idx < N:
                    arr[i].left = arr[i*2 + 1 - null_count*2]
                if right_idx < N:
                    arr[i].right = arr[i*2 + 2 - null_count*2]
        
        return arr[0]
