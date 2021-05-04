# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    # BFS for both serialize and deserialize [O(n), 89%]
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        print("serialize:")
        
        if not root:
            return ""
        
        deq = deque([root])
        dataList = [str(root.val)]
        while deq:
            for _ in range(len(deq)):
                cur = deq.popleft()
                if cur.left:
                    deq.append(cur.left)
                    dataList.append(cur.left.val)
                else:
                    dataList.append("#")
                    
                if cur.right:
                    deq.append(cur.right)
                    dataList.append(cur.right.val)
                else:
                    dataList.append("#")
            
        #print(root)
        data = " ".join([str(x) for x in dataList])
        print(data)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print("deserialize:")
        if not data:
            return None
        
        dataList = data.split(" ")  #list 
        root = TreeNode(int(dataList[0]))
        deq = deque([root])
        idx = 1 #idx of list
        
        while deq:
            cur = deq.popleft()
            
            #Get a val for the left  
            if idx >= len(dataList):
                break
            nodeVal = dataList[idx]
            if nodeVal != "#":
                cur.left = TreeNode(int(nodeVal))
                deq.append(cur.left)
            idx += 1  # incremental even it's "#"
                
            #Get a val for the right  
            if idx >= len(dataList):
                break
            nodeVal = dataList[idx]
            if nodeVal != "#":    
                cur.right = TreeNode(int(nodeVal))
                deq.append(cur.right)
            idx += 1  # incremental even it's "#"
        
        #print(root)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))