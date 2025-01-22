# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        print("2")
        def getHeightOrUnbalanced(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_height = getHeightOrUnbalanced(root.left) 
            right_height = getHeightOrUnbalanced(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return getHeightOrUnbalanced(root) != -1

    # 
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        print("1")
        def helper(root) -> (bool, int):
            if root is None:
                return True, 0
            left_result, left_height = helper(root.left) 
            right_result, right_height = helper(root.right)
            if left_result and right_result and abs(left_height - right_height) <= 1:
                return True, max(left_height, right_height) + 1
            else:
                return False, -1
        return helper(root)[0]