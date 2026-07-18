# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser_list = []
        def preorder(root):
            if not root:
                ser_list.append('n')
            else:
                ser_list.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return ",".join(ser_list)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        d_list = data.split(',')
        index = [0]

        def preorder():
            curr = d_list[index[0]]
            index[0] += 1

            if curr == 'n':
                return None
            
            root = TreeNode(int(curr))
            root.left = preorder()
            root.right = preorder()
            return root
        
        return preorder()