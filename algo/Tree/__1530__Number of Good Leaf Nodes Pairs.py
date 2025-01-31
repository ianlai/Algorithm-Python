# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # DFS [O(n): 56%]
    # Return an array to contain the number of distance from node to leave
    # e.g. [0,2,2] 
    # dist = 1 : 0 nodes 
    # dist = 2 : 2 nodes 
    # dist = 3 : 2 nodes 
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root is None:
            return 0
        self.total = 0
        def dfs(node, distance):
            if node.left and node.right:
                left = dfs(node.left, distance)
                # Can't use sum(left) == 0 to check 
                # because it will happen when the hight larger than distance (pop out)
                # if sum(left) == 0:  
                if left is None:
                    left = [0] * distance
                    left[0] = 1
                else:
                    left.insert(0, 0)
                    left.pop()
                
                right = dfs(node.right, distance)
                if right is None:
                    right = [0] * distance
                    right[0] = 1
                else:
                    right.insert(0, 0)
                    right.pop()
                
                #calculate the path distance and update to global var
                for i in range(len(left)):
                    for j in range(len(right)):
                        sumLength = (i+1) + (j+1)
                        if sumLength > distance:
                            break
                        self.total += left[i] * right[j] 
                
                #update return array 
                for i in range(len(left)):
                    left[i] = left[i] + right[i]
                return left
                
            elif node.left:
                left = dfs(node.left, distance)
                if left is None:
                    left = [0] * distance
                    left[0] = 1
                else:
                    left.insert(0, 0)
                    left.pop()
                return left
                
            elif node.right:
                right = dfs(node.right, distance)
                if right is None:
                    right = [0] * distance
                    right[0] = 1
                else:
                    right.insert(0, 0)
                    right.pop()
                return right
            else:
                return None  #leaf 
            #Error
            print("Error")
            
        dfs(root, distance)
        return self.total
            