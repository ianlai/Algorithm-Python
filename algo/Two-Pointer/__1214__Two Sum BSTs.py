# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Two Sum [O(n+m): 96%]
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        arr1 = self.getSortedArray(root1)
        arr2 = self.getSortedArray(root2)
        
        p1, p2 = 0, len(arr2) - 1
        while p1 < len(arr1) and p2 >= 0:
            twoSum = arr1[p1] + arr2[p2]
            if twoSum == target:
                return True
            if twoSum < target:
                p1 += 1
            if twoSum > target:
                p2 -= 1
        return False
    
    def getSortedArray(self, root):
        arr = []
        self.inorder(root, arr)
        return arr
    
    def inorder(self, root, arr):
        if not root:
            return 
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
    
    # ======================================================
    # Two splits [TLE]
    def twoSumBSTs1(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1:
            return False
        if not root2:
            return False
        
        twoSum = root1.val + root2.val
        if twoSum == target:
            return True
        
        if twoSum < target:
            if self.twoSumBSTs(root1.right, root2, target):
                return True
            if self.twoSumBSTs(root1, root2.right, target):
                return True
            
        if twoSum > target:
            if self.twoSumBSTs(root1.left, root2, target):
                return True
            if self.twoSumBSTs(root1, root2.left, target):
                return True
            
        return False