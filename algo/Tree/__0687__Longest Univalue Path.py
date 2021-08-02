# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursive with global variable [O(n), 64%]
    def longestUnivaluePath(self, root: TreeNode) -> int:
        print("Method-0")
        self.longest = 0 
        self.find(root)
        return self.longest 
    
    def find(self, root):
        if not root:
            return 0
        
        consecutiveL = self.find(root.left)
        consecutiveR = self.find(root.right)
        
        consecutiveL = consecutiveL + 1 if root.left and root.val == root.left.val else 0
        consecutiveR = consecutiveR + 1 if root.right and root.val == root.right.val else 0
            
        self.longest = max(self.longest, consecutiveL + consecutiveR)
        #print("root:", root.val)
        #print("longest:", self.longest)
        #print("longestConsecutive:", max(consecutiveL, consecutiveR) )
        return max(consecutiveL, consecutiveR) 
    
    # =============================================
        
    # Recursive with two return values [O(n): 21%]
    def longestUnivaluePath1(self, root: TreeNode) -> int:
        print("Method-1")
        if not root: 
            return 0
        consecutiveCur, longestCur = self.findLongest(root)
        
        return max(consecutiveCur, longestCur)

    def findLongest(self, root):
        if not root:
            return 0, 0
        consecutiveL, longestL = self.findLongest(root.left)
        consecutiveR, longestR = self.findLongest(root.right)

        longestCur = max(longestL, longestR)

        consecutiveCur = 0
        
        if root.left and root.right and root.left.val == root.val == root.right.val:
            longestCur = max(longestCur, consecutiveL + consecutiveR + 2)
            consecutiveCur = max(consecutiveL, consecutiveR) + 1
        else:
            if root.left and root.left.val == root.val:
                consecutiveCur = consecutiveL + 1
            if root.right and root.right.val == root.val:
                consecutiveCur = max(consecutiveR + 1, consecutiveL)

        longestCur = max(longestCur, consecutiveCur)
        return consecutiveCur, longestCur