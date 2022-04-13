# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ===============================================
    # 2022/04/13
    # Not passing slice + Not using index() [O(n): 90%]
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        print("Code3")
        
        def helper(left, right):
            if left > right:
                return None
            node = TreeNode(postorder.pop())
            #idx = inorder.index(node.val)
            idx = valToIdx[node.val]
            
            node.right = helper(idx+1, right)
            node.left = helper(left, idx-1)
            return node 
        
        valToIdx = {}
        for i, v in enumerate(inorder):
            valToIdx[v] = i
            
        return helper(0, len(inorder)-1)
        
    # ===============================================
    # 2022/04/13
    # Not passing slice [O(n): 63%]
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        print("Code2")
        
        def helper(left, right):
            if left > right:
                return None
            node = TreeNode(postorder.pop())
            idx = inorder.index(node.val)
            
            node.right = helper(idx+1, right)
            node.left = helper(left, idx-1)
            return node 
        
        return helper(0, len(inorder)-1)
        
    # ===============================================
    # 2022/04/12
    # Using slice, improvable  [O(n2): 20%]
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        print("Code1")
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