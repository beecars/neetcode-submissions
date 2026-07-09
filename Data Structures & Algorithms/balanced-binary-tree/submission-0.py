# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0] # [Balanced, Height]

            lb, lh = dfs(root.left)
            rb, rh = dfs(root.right)
            
            if lb and rb and abs(lh - rh) <= 1:
                balanced = True
            else:
                balanced = False
            

            return [balanced, 1 + max(lh, rh)]

        return dfs(root)[0]