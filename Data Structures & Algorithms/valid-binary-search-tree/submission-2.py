# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sorted_list = self.inorder(root)

        for i in range(1, len(sorted_list)):
            if sorted_list[i] <= sorted_list[i - 1]:
                return False
        return True

    def inorder(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        res = []
        dfs(root)
        return res
    
