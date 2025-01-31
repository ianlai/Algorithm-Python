# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/03/25 
    # Find predecessor or successor then replace the deleted one [O(logn): 43%]
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        print("Code2")
        
        #One step left than go straight to the rightmost 
        def findPredecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val
        
        #One step right than go straight to the leftmost 
        def findSuccessor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val
            
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Going to either side is fine
            if root.left:
                root.val = findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = findSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = None   
        return root 
            
    # =========================================
    
    # 2021/08/06 
    # Find target's parent, remove target, if two subtrees then merge [O(logn): 75%]
    def deleteNode1(self, root: TreeNode, key: int) -> TreeNode:
        print("Code1")
        def findParent(root, key):
            cur = root
            if cur and key < cur.val:
                if cur.left and key == cur.left.val:
                    return cur
                if cur.left:
                    return findParent(cur.left, key)
            
            elif cur and key > cur.val:
                if cur.right and key == cur.right.val:
                    return cur
                if cur.right:
                    return findParent(cur.right, key)

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
            if not right:
                return left
            
            #Merge right to left; return left
            left.right = mergeNodes(left.right, right)
            return left
                    
        dummy = TreeNode(float('inf'))
        dummy.left = root
        parent = findParent(dummy, key)
        remove(parent, key)
        
        return dummy.left