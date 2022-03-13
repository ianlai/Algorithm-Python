# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #2022/03/13
    #Pass the ranges [O(n): 83%]
    def isValidBST(self, root: TreeNode) -> bool:
        print("Code3")
        def isValidBST(node, minVal, maxVal):
            if node is None:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            left = isValidBST(node.left, minVal, node.val)
            if not left:
                return False
            right = isValidBST(node.right, node.val, maxVal)
            if not right:
                return False
            return True
            
        return isValidBST(root, -inf, inf)
    
    # ================================================
    
    # 2021/04/22
    # Inorder traversal 
    def isValidBST(self, root: TreeNode) -> bool:
        print("Code2: Inorder")
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
    
    # ================================================
    # 2021/04/22
    # Calculate the valid interval [O(n): 6%]
    def isValidBST(self, root: TreeNode) -> bool:
        print("Code1: Min-Max interval")
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
        