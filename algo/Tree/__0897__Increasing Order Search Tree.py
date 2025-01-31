# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/17
    # Inorder, push the nodes instead of creating nodes again [Time: O(N): 68% / Space: O(H): 50%]
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return root
        
        def inorderTraverse(node, inorder):
            if not node:
                return node
            inorderTraverse(node.left, inorder)
            inorder.append(node)
            inorderTraverse(node.right, inorder)
        
        def generateIncreasingBST(inorder):
            dummy = TreeNode()
            cur = dummy 
            for node in inorder:
                cur.left = None
                cur.right = node
                cur = cur.right
            cur.left = None
            cur.right = None
            return dummy.right 
            
        inorder = []
        inorderTraverse(root, inorder)
        root = generateIncreasingBST(inorder)
        return root 