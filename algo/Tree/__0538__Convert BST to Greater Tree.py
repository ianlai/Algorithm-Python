# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DESC traversal [O(n): 58%]
    def convertBST(self, root: TreeNode) -> TreeNode:
        print("DESC traversal")
        self.largerSum = 0
        self.dfs(root)
        return root
    
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        temp = root.val 
        root.val += self.largerSum
        self.largerSum += temp 
        self.dfs(root.left)
        
    # ========================================
    
    # Two-step divide and conquer [O(n): 58%]  
    def convertBST(self, root: TreeNode) -> TreeNode:
        print("Two step ")
        if not root:
            return root
        
        self.helper1(root)
        self.helper2(root, 0)
        return root
    
    # add the right subtree 
    def helper1(self, root):
        if not root:
            return 0
        r = self.helper1(root.right)
        root.val += r        #root's val becomes sum of root and sum of root's right (root + right) 
        l = self.helper1(root.left) 
        return root.val + l  #return val is sum of the root's subtree (left + root+ right)
    
    # add the right parent
    def helper2(self, root, parentVal):
        if not root:
            return 
        root.val += parentVal 
        self.helper2(root.left, root.val)
        self.helper2(root.right, parentVal)
        return 