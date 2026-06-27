# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        
        big_list = []

        while q:
            small_list = []
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    small_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if small_list:
                big_list.append(small_list)
        
        return big_list