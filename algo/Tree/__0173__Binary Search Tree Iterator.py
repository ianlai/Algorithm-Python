# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    
    # Iterative inorder traversal [O(n), 90%]
    def __init__(self, root: TreeNode):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next() #From dummy to root

    def next(self) -> int:
        cur = self.stack.pop()  
        nextNode = cur  #keep current node at cur so that we can return 
        
        if not nextNode:      
            return -1  #shouldn't reach this line 
        
        #Core logic
        if nextNode.right:
            nextNode = nextNode.right
            while nextNode:
                self.stack.append(nextNode)
                nextNode = nextNode.left
                
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()