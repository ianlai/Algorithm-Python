# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/12
    # Using slice, improvable  [O(n2): 20%]
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None 
        
        post = postorder[-1]
        idx = inorder.index(post)
        left = inorder[:idx]
        right = inorder[idx+1:]
        leftPost = postorder[:len(left)]
        rightPost = postorder[len(left):len(postorder)-1]
        
        root = TreeNode(post)
        root.left = self.buildTree(left, leftPost)
        root.right = self.buildTree(right, rightPost)
        return root 