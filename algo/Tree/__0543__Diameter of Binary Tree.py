# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0        
        diameter, _ = self.helper(root)
        return diameter
        
    def helper(self, root):
        if not root:
            return 0
        #print(root.val)
        
        thisDiameter = 0  #case1: diameter passing this root
        leftDiameter = 0  #case2: max diameter from left's point of view
        rightDiameter = 0 #case3: max diameter from right's point of view 
        maxDiameter = 0   #max diameter from this root's point of view 
        
        leftHeight = 0 
        rightHeight = 0
        maxHeight = 0
        
        if root.left:
            leftDiameter, leftHeight = self.helper(root.left)
            thisDiameter += 1 + leftHeight
            #print(" ", root.val, " -> left:", leftDiameter, leftHeight)
        if root.right:
            rightDiameter, rightHeight = self.helper(root.right)
            thisDiameter += 1 + rightHeight
            #print(" ", root.val, " -> right:", rightDiameter, rightHeight)
        
        maxDiameter = max(thisDiameter, leftDiameter, rightDiameter) #calculate the max diameter from this root's point of view
        
        if root.left or root.right:
            maxHeight = max(leftHeight, rightHeight) + 1  #calculate the height of this root
        #print(" ", root.val, " ==> ", maxDiameter, maxHeight)
        return maxDiameter, maxHeight