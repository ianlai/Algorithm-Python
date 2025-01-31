# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        heads = []
        to_delete = set(to_delete)

        self.findHeaders(root, to_delete, heads, False)
        #print([head.val for head in heads])
        for head in heads:
            self.delete(head, to_delete)
        return heads
    
    def findHeaders(self, root, to_delete, heads, isHead):
        if not root:
            return 
        if root.val in to_delete:
            isHead = False
        else:
            if not isHead:
                isHead = True  #new head
                heads.append(root)
        self.findHeaders(root.left, to_delete, heads, isHead)
        self.findHeaders(root.right, to_delete, heads, isHead)
        
    def delete(self, root, to_delete):
        if not root:
            return
        #print(root.val)
        if root.left and root.left.val in to_delete:
            root.left = None
        if root.right and root.right.val in to_delete:
            root.right = None
        self.delete(root.left, to_delete)
        self.delete(root.right, to_delete)