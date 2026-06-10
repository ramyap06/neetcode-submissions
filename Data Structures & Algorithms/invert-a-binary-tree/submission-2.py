# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        # swap children
        new_right = root.left
        root.left = root.right
        root.right = new_right

        # once the recursion finishes return the root
        return root