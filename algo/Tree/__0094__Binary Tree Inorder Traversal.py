# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #Morris [Time: O(n) / Space: O(1)]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        print("Morris")
        if not root:
            return []
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right 
            else:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root  #virtual link
                tmp = root
                root = root.left 
                tmp.left = None
        return res
    
    # Iterative  [Time: O(n) / Space: O(n)]
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        print("Iterative")
        if not root:
            return []
        
        res = []
        stack = []
        while root or stack: 
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right 
        return res
    
    
    # Recursive  [Time: O(n) / Space: O(n)]
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        print("Recursive")
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    # Example: 
    #                1
    #            2 
    #        3    4
    #         5 
    
    # Iterative (52%)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        print("Iterative")
        if not root:
            return []
        
        stack = []   #node 
        arr = []     #val
        
        cur = root
        while stack or cur:
            # cur = stack.pop()  #no, we can't take this out 
            while cur:
                # (1) insert the root of the tree/subtree (go left)
                stack.append(cur)  
                cur = cur.left     #Up part: 1 -> 2 -> 3 (out order: 3 -> 2 -> 1)
                
            # (2) last cur var is abandoned (None); get the first from pop (leftmost)
            cur = stack.pop()      #Down part: 3 (middle)
            arr.append(cur.val)    #Down part: 3 (middle)

            # (3) since the middle is added into arr, we can go right then 
            cur = cur.right        #Down part: 5 (right) 
            
        return arr
    
    #=====================================================
    
    # Recursive
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        print("Recursive")
        if not root:
           return []
        
        arr = []
        self.inorder(root, arr)
        return arr
    
    def inorder(self, root, arr):
        if not root:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)