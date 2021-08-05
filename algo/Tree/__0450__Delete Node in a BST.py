# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def findTarget(root, key):
            cur = root
            if cur and key < cur.val:
                if cur.left and key == cur.left.val:
                    return cur
                if cur.left:
                    return findTarget(cur.left, key)
            
            elif cur and key > cur.val:
                if cur.right and key == cur.right.val:
                    return cur
                if cur.right:
                    return findTarget(cur.right, key)

            elif not cur:
                return -1  # can't find
        
        def remove(parent, key):
            if parent and parent.val > key:  #left
                parent.left = mergeNodes(parent.left.left, parent.left.right)
            elif parent and parent.val < key:  #right
                parent.right = mergeNodes(parent.right.left, parent.right.right)
            
        def mergeNodes(left, right):
            if not left: 
                return right
            if left.right:
                left.right = mergeNodes(left.right, right)
            else:
                left.right = right
            return left
                    
        dummy = TreeNode(float('inf'))
        dummy.left = root
        parent = findTarget(dummy, key)
        remove(parent, key)
        
        return dummy.left