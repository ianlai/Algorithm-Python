# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/15
    # Tree conversion recursively; helper function removed [O(n) 95%]
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        print("Code2")
    
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
            
            
    # 2022/04/15
    # Tree conversion recursively [O(n) 67%]
    def trimBST1(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        print("Code1")
        def _trimBST(node):
            if node is None:
                return None
            
            if node.right:
                if node.right.val > high:
                    node.right = _trimBST(node.right.left)
                else:
                    node.right = _trimBST(node.right)

            if node.left:                
                if node.left.val < low:
                    node.left = _trimBST(node.left.right)
                else:
                    node.left = _trimBST(node.left)
                    
            if node.val > high:
                return _trimBST(node.left)
            if node.val < low:
                return _trimBST(node.right)
            return node 
        return _trimBST(root)