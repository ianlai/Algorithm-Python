# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Inorder: [35%]  
    
    # O(n) 
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def inorder(root):
            if root is None:
                return ""
            serializedStr = str(root.val) 
            if root.left is not None:
                serializedStr += "," + inorder(root.left) 
            if root.right is not None:
                serializedStr += "," + inorder(root.right)     
            return serializedStr
        return inorder(root) if root is not None else ""

    # O(n) 
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def _deserialize(dataList): 
            if len(dataList) == 0 or len(dataList[0]) == 0:
                return None   

            head = TreeNode(int(dataList[0]))
            for i in range(1, len(dataList)):
                s = int(dataList[i])
                if s > head.val:
                    if i > 1:
                        head.left = _deserialize(dataList[1:i])
                        head.right = _deserialize(dataList[i:])
                        return head
                    else:
                        head.right = _deserialize(dataList[i:])
                        return head
            head.left = _deserialize(dataList[1:])
            return head
        
        dataList = data.split(",")
        return _deserialize(dataList)
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans