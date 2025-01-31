# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 2022/01/04
    # Binary Search [O(log^2n): 30%]
    def countNodes(self, root: TreeNode) -> int:
        cur = root
        left = 0
        while cur:
            cur = cur.left
            left += 1
        
        cur = root
        right = 0
        while cur:
            cur = cur.right
            right += 1
        
        print("left, right:", left, right)
        res = 0
        if left == right:
            res = 2 ** left - 1
            return res        
        
        def isSameAsLeft(val):
            #valBin = bin(val)[2:]
            valBin = format(val, "0" + str(right) + "b")
            #valBin = "{0:b}".format(val)
            #print(valBin)
            cur = root
            for i, v in enumerate(valBin):
                if v == "0":
                    if not cur.left:
                        return False
                    cur = cur.left
                else:
                    if not cur.right:
                        return False
                    cur = cur.right
            return True
        
        # for i in range(16):
        #     print(i, ":", isSameAsLeft(i))
            
        start, end = 0, 2 ** (left - 1)
        while start < end:
            mid = start + (end - start) // 2
            if isSameAsLeft(mid):
                start = mid + 1
            else:
                end = mid
        
        upper = 2 ** right - 1
        last = start
        res = upper + last
        return res