# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Linear search [O(n2): 76%]
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        firstRight = 0 
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                firstRight = i
                break 
        if firstRight != 0:
            root.left = self.bstFromPreorder(preorder[1:firstRight])
            root.right = self.bstFromPreorder(preorder[firstRight:])
        else:
            root.left = self.bstFromPreorder(preorder[1:])
        return root