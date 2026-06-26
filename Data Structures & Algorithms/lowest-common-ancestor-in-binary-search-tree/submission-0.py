# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        if p.val <= root.val and q.val >= root.val or p.val >= root.val and q.val <= root.val:
            return lca
        
        if p.val > root.val and q.val > root.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)

        return lca