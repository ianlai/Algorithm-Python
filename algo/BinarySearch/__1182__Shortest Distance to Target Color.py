class Solution:
    
    # 2022/03/05
    # Map + Binary Search [O(N + Q*log(N)]: 81%
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        ##Generate the map 
        colorToIndices = collections.defaultdict(list)
        for i, color in enumerate(colors):
            colorToIndices[color].append(i)
        print(colorToIndices)
        
        ##Left BS for distance 
        def binarySearchLeft(arr, target):
            if len(arr) == 0:
                return -1
            start, end = 0, len(arr)
            while start < end:
                mid = start + (end - start) // 2
                if arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid
                    
            # Return the distance (diff between val, not index)
            if start == 0:
                return abs(arr[start] - target)
            if start == len(arr):
                return abs(arr[start - 1] - target)
            return min(abs(arr[start - 1] - target) , abs(arr[start] - target))
            
        ## Traverse the queries 
        res = []
        for i, c in queries:
            distance = binarySearchLeft(colorToIndices[c], i)
            res.append(distance)
        return res