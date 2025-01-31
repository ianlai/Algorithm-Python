# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    #Inorder Traversal [O(n): 34%]
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        arr = []
        self.helper(root, arr)
        index = arr.index(p)
        return arr[index+1] if index != len(arr) - 1 else None
    
    def helper(self, root, arr):
        if root is None:
            return 
        self.helper(root.left, arr)
        arr.append(root)
        self.helper(root.right, arr)