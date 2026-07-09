# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pnodes = deque()
        pnodes.append(p)
        qnodes = deque()
        qnodes.append(q)

        while pnodes:

            a_pnode = pnodes.popleft()
            a_qnode = qnodes.popleft()

            if not a_pnode and not a_qnode:
                continue
            if not a_pnode or not a_qnode:
                return False
            if a_pnode.val != a_qnode.val:
                return False

            pnodes.append(a_pnode.left)
            qnodes.append(a_qnode.left)
            pnodes.append(a_pnode.right)
            qnodes.append(a_qnode.right)
            
        return True