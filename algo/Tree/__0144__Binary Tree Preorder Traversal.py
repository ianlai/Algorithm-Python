# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Iterative [53%]
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        print("Iterative")
        if not root:
            return []
        
        stack = [root] #node 
        arr = []       #val
        
        while stack:
            cur = stack.pop()
            arr.append(cur.val)         #(1) middle
            if cur.right:
                stack.append(cur.right) #(2) right (reversed!)
            if cur.left:
                stack.append(cur.left)  #(3) left  (reversed!)
        return arr
    
    #=====================================================
    
    # Recursive [53%]
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        print("Recursive")
        if not root:
            return []    

        ans = []       #val
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if not root:
            return
        ans.append(root.val)         #(1) middle
        self.helper(root.left, ans)  #(2) left
        self.helper(root.right, ans) #(3) right
        return 
        
    