# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Inorder than form BST [O(n): 30%]
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        sortedList = []
        self.inorder(root, sortedList)        
        return self.formBST(sortedList)
    
    def inorder(self, root, sortedList):
        if not root:
            return
        self.inorder(root.left, sortedList)
        sortedList.append(root.val)
        self.inorder(root.right, sortedList)
    
    def formBST(self, arr):
        if not arr:
            return 
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.formBST(arr[:mid])
        root.right = self.formBST(arr[mid+1:])
        return root

    #============================================    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        sortedList = []
        self.inorder(root, sortedList)        
        res = TreeNode()
        self.formBST(res, sortedList)
        return res
    
    def inorder(self, root, sortedList):
        if not root:
            return
        self.inorder(root.left, sortedList)
        sortedList.append(root.val)
        self.inorder(root.right, sortedList)
    
    def formBST(self, root, arr):
        if not arr:
            return 
        mid = len(arr) // 2
        root.val = arr[mid]
        if mid > 0:
            root.left = TreeNode()
            self.formBST(root.left, arr[:mid])
        if mid + 1 < len(arr):   
            root.right = TreeNode()
            self.formBST(root.right, arr[mid+1:])