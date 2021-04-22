# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # === Inorder traversal (BST should be ascending)
    def isValidBST(self, root: TreeNode) -> bool:
        print("Inorder")
        if not root:
            return False
        
        arr = []
        self.inorder(root, arr)
        #print(arr)
        
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False
        return True
        
    def inorder(self, root, arr):
        if not root:
            return 
        #print(root.val, arr)

        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        return 
    
    # === Calculate the valid interval (6%)
    def isValidBST1(self, root: TreeNode) -> bool:
        print("Min-Max interval")
        if not root:
            return False
        maxVal = float("inf")
        minVal = -float("inf")
        
        return self.isValidNode(root.right, root.val, maxVal) and \
            self.isValidNode(root.left, minVal, root.val)

    def isValidNode(self, node, minVal, maxVal):
        if not node:
            return True
        if node.val <= minVal:
            return False
        if node.val >= maxVal:
            return False
        
        return self.isValidNode(node.right, node.val, maxVal) and \
            self.isValidNode(node.left, minVal, node.val)
                
        
    # === Chech all nodes the BST condition (incorrect, because root.right.left might be smaller than root)
    
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     if root.left and root.val <= root.left.val:
    #         return False
    #     if root.right and root.val >= root.right.val:
    #         return False
    #     return self.isValidBST(root.left) and self.isValidBST(root.right)
        