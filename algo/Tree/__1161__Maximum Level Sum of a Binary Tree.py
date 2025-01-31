# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        deq = collections.deque([(root, 1)])
        layerSums = collections.defaultdict(int)
        while deq:
            cur, layer = deq.popleft()
            layerSums[layer] += cur.val
            if cur.left:
                deq.append((cur.left, layer + 1))
            if cur.right:
                deq.append((cur.right, layer + 1))
        
        maxLayerSum = -inf
        maxLayers = []
        for layer, layerSum in layerSums.items():
            if layerSum > maxLayerSum:
                maxLayerSum = layerSum
                maxLayers = []
                maxLayers.append(layer)
            elif layerSum == maxLayerSum:
                maxLayers.append(layer)
        return min(maxLayers)