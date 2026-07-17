# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [root.val]

        def postorder(root):
            if not root:
                return 0
            
            max_left = postorder(root.left)
            max_right = postorder(root.right)

            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            max_path[0] = max(max_path[0], root.val + max_left + max_right)
            
            return root.val + max(max_left, max_right)
        
        postorder(root)
        return max_path[0]