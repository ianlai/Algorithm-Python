# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Memoization DP [93% / 94%]
    # Divide and Conquer [63% / 60%]
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []
        memo = {}
        return self.generateTreesInterval(1, n, memo)
        
    def generateTreesInterval(self, s, e, memo):
        if s > e:
            return None
        if s == e:
            return [TreeNode(s)]
        if (s, e) in memo:
            return memo[(s, e)]
        
        #print(s, e)
        results = []
        for i in range(s, e+1):
            cur = TreeNode(i)
            left = self.generateTreesInterval(s, i-1, memo)
            right = self.generateTreesInterval(i+1, e, memo)
            if not right and not left:
                results.append(cur)
                
            elif not right:
                for l in left:
                    cur = TreeNode(i)
                    cur.left = l
                    results.append(cur)
                
            elif not left:
                for r in right:
                    cur = TreeNode(i)
                    cur.right = r
                    results.append(cur)
            
            elif right and left:
                for r in right:
                    for l in left:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        results.append(cur)
        #print(results)
        memo[(s, e)] = results
        return results