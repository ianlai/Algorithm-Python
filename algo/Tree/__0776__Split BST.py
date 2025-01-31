# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2021/12/19
    # Recursion [O(logn): 67%]  //difficult
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        print("Code2")
        if root is None:
            return [None, None]
        
        print(root.val)
        if target == root.val:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        elif target < root.val:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]
        else:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
    
    # ====================================================
    # Incorrect
    def splitBST1(self, root: TreeNode, target: int) -> List[TreeNode]:
        print("Code1")
        
        preHead = TreeNode(-inf, None, root)
        parentNode, targetNode = self.findTarget(preHead, target)
        print(parentNode.val, targetNode.val)
        
        if targetNode.val < parentNode.val:
            parentNode.left = targetNode.right
            targetNode.right = None
            return [targetNode, root]
        else:
            rightNode = targetNode.right
            targetNode.right = None
            return [root, rightNode]
        
    def findTarget(self, head, target):
        if target < head.val:
            if not head.left:
                return None, None
            if target == head.left.val:
                return head, head.left
            elif target < head.left.val:
                return self.findTarget(head.left, target) 
            else:
                return self.findTarget(head.left, target)
        elif target > head.val: 
            if not head.right:
                return None, None
            if target == head.right.val:
                return head, head.right
            elif target < head.right.val:
                return self.findTarget(head.right, target)
            else:
                return self.findTarget(head.right, target)
        else:
            print("ERROR")
            
        
        
