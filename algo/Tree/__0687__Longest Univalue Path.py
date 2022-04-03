# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/03
    # DFS [O(n): 96%]
    # - Return longest length to current node
    # - Use global to track real longest path 
    def longestUnivaluePath(self, root: TreeNode) -> int:
        print("Code3")
        if root is None:
            return 0
        self.longest = 0
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            res = 0
            if not node.left and not node.right: 
                res = 0
            elif not node.left:
                if node.val == node.right.val:
                    res = right + 1
                self.longest = max(self.longest, res)
            elif not node.right:
                if node.val == node.left.val:
                    res = left + 1
                self.longest = max(self.longest, res)
            else:
                if node.left.val == node.right.val:
                    if node.val == node.left.val:
                        res = max(left, right) + 1 
                        self.longest = max(self.longest, left + right + 2)
                else:
                    if node.val == node.right.val:
                        res = right + 1
                    if node.val == node.left.val:
                        res = left + 1
                    self.longest = max(self.longest, res)
            return res
        helper(root)
        return self.longest

    # =============================================
    # 2021/08/01
    # Recursive with global variable [O(n), 64%]
    def longestUnivaluePath2(self, root: TreeNode) -> int:
        print("Code2")
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
        
    # 2021/07/29
    # Recursive with two return values [O(n): 21%]
    def longestUnivaluePath1(self, root: TreeNode) -> int:
        print("Code1")
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