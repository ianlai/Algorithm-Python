# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def minCameraCover(self, root):
    #     self.res = 0
    #     def dfs(root):
    #         if not root: return 2
    #         l, r = dfs(root.left), dfs(root.right)
    #         if l == 0 or r == 0:
    #             self.res += 1
    #             return 1
    #         return 2 if l == 1 or r == 1 else 0
    #     return (dfs(root) == 0) + self.res
    
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0 
        def postOrder(root):
            nonlocal count 
            if root is None:
                return 2
            left = postOrder(root.left)
            right = postOrder(root.right)
            if left == 0 or right == 0:
                count += 1
                return 1
            if left == 1 or right == 1:
                return 2
            return 0 
        return (postOrder(root) == 0) + count
        #return count if count != 0 else 1 
    
    # def minCameraCover(self, root: Optional[TreeNode]) -> int:
    #     count = 0 
    #     def postOrder(root):
    #         nonlocal count 
    #         if root is None:
    #             return -1
    #         left = postOrder(root.left)
    #         right = postOrder(root.right)
    #         res = max(left, right) + 1
    #         if res == 1:
    #             count += 1
    #             print(root.val)
    #             return -2 
    #         else:
    #             return res
    #     postOrder(root)
    #     return count if count != 0 else 1 
#     def minCameraCover(self, root: Optional[TreeNode]) -> int:
#         count = 0 
#         def postOrder(root):
#             nonlocal count 
#             left, right = 0, 0
#             if not root.left and not root.right:
#                 return 0
#             elif not root.left:
#                 right = postOrder(right)
#             elif not root.right:
#                 left = postOrder(left)
#             else:
#                 right = postOrder(right)
#                 left = postOrder(left)
                
#             if left == 1 or right == 1:
#                 count += 1
#                 return -1
                
    
    

        