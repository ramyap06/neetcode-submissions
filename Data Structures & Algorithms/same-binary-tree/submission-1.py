# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        left_res = self.isSameTree(p.left, q.left)
        right_res = self.isSameTree(p.right, q.right)
        
        if p.val != q.val:
            return False

        if not left_res or not right_res:
            return False
        else:
            return True