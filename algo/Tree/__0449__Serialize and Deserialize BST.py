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
        def inorder(root) -> str:
            if root is None:
                return ""
            serializedStr = str(root.val) 
            if root.left is not None:
                serializedStr += "," + inorder(root.left) 
            if root.right is not None:
                serializedStr += "," + inorder(root.right)     
            return serializedStr
        res = inorder(root) if root is not None else ""
        print(res)
        return res

    # O(n) 
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def _deserialize(dataList): 
            if len(dataList) == 0 or len(dataList[0]) == 0:
                return None   

            head = TreeNode(int(dataList[0]))
            firstLargerIdx = 1
            for i in range(1, len(dataList)):
                s = int(dataList[i])
                firstLargerIdx = i
                if s > head.val:
                    break
                    
            #print(head, "->", dataList, firstLargerIdx)
            
            if firstLargerIdx == 1:
                if int(dataList[-1]) > head.val:
                    head.right = _deserialize(dataList[1:])
                else:
                    head.left = _deserialize(dataList[1:])
            else: 
                if int(dataList[-1]) > head.val:
                    head.left = _deserialize(dataList[1:i])
                    head.right = _deserialize(dataList[i:])
                else:
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