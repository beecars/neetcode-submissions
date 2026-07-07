# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        nodes = deque()

        if root:
            nodes.append(root)
        
        while nodes:
            max_depth += 1
            for _ in range(len(nodes)):
            
                popnode = nodes.popleft()

                if popnode.left:
                    nodes.append(popnode.left)
                if popnode.right:
                    nodes.append(popnode.right)

        return max_depth