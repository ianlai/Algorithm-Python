# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''
           9
         8
       7
     6
        pre = [9,8,7,6]
        in  = [6,7,8,9]
    '''
    # 2022/07/14
    # Recursive [TC: O(N^2): 24% / SC: O(N+2N): 7%] 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        print("Code2")
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:rootIdx+1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])
        return root


    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        h = preorder[0]
        root = TreeNode(h)
        idx = inorder.index(h)
        sizeL = len(inorder[:idx])
        sizeR = len(inorder[idx+1:])
        root.left = self.buildTree(preorder[1:sizeL+1], inorder[:idx])
        root.right = self.buildTree(preorder[sizeL+1:], inorder[idx+1:])
        return root