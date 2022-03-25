# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/03/25
    # Recursion [Avg time: O(logn): 82% / Worst time: O(n2)]
    # Remember we need the relationship between two levels 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        else:
            if val < root.val:
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        return root