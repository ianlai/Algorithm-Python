# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/07/04
    # Inorder + TwoSum [O(n+n): 23% / O(n): 12%]
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            return 
        def twoSum(arr, k):
            if len(arr) <= 1:
                return False
            left, right = 0, len(arr) - 1
            while left < right:
                s = arr[left] + arr[right]
                if s == k:
                    return True
                elif s < k:
                    left += 1
                else:
                    right -= 1
            return False
            
        inorder(root)
        return twoSum(arr, k)
    