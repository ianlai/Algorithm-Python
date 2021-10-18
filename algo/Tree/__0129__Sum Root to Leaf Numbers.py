# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursive DFS [Time O(N): 71% ; Space O(H): 49% ]
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = self.helper(root)
        res = 0
        for path in arr:
            res += int(path)
        return res
    def helper(self, root):
        arr = []     
        if not root.left and not root.right:
            arr.append(str(root.val))
        else:
            if root.left:
                leftArr = self.helper(root.left)
                for left in leftArr:
                    arr.append(str(root.val) + left)
            if root.right:
                rightArr = self.helper(root.right)   
                for right in rightArr:
                    arr.append(str(root.val) + right)
        return arr