# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 2022/04/14
    # Iteration [O(logn): 80%]
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print("Code2")
        
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root 
        
        
    # 2022/03/25
    # Recursion [O(logn): 25%]
    def searchBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print("Code1")
        if root is None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
            