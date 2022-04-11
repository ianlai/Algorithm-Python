# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/11
    # Pre-order + Post-order; recursive call [O(n): 26%]
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        #print(pre, post)
        if len(pre) == 0:
            return None
        
        # 1 node
        root = TreeNode(pre[0])
        
        # 2 nodes 
        if len(pre) >= 2:
            left = pre[1]
            
            leftIdx = post.index(left)
            leftPost = post[:leftIdx+1]
            leftPre = pre[1:leftIdx+2]
            
            root.left = self.constructFromPrePost(leftPre, leftPost)
            root.right = None
        
        # 3 nodes or more
            if len(pre) >= 3:
                rightPost = post[leftIdx+1:len(post)-1]
                rightPre = pre[leftIdx+2:]
                
                root.right = self.constructFromPrePost(rightPre, rightPost)
            
        return root