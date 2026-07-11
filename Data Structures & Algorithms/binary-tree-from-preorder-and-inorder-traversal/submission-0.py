# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        print("start:", preorder[0], )
        root = TreeNode(preorder[0])
        mid = 0
        n = len(inorder)

        for i in range(n):
            if inorder[i] == preorder[0]:
                mid = i
                break
        
        print("mid:", preorder[mid], inorder[mid])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root