# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        if not root:
            return max_depth
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        max_depth = 1 + max(left_depth, right_depth)

        return max_depth