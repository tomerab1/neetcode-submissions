# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_q = [q]
        q_p = [p]

        while q_q and q_p:
            n_q = q_q.pop(0)
            n_p = q_p.pop(0)

            if not n_q and not n_p:
                continue
            if not (n_q and n_p) or (n_q.val != n_p.val):
                return False
            
            q_q.append(n_q.left)
            q_p.append(n_p.left)
            q_q.append(n_q.right)
            q_p.append(n_p.right)
        
        return True



        