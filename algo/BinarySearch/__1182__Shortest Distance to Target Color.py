class Solution:
    
    # 2022/03/05
    # DP: Fill distances in table [O(N+Q): 33%] 
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        print("Code3")
        dp = [[inf] * 3 for _ in range(len(colors))]
        
        # Forward-traverse
        lastIdx = [-1] * 3
        for i in range(len(colors)):
            c = colors[i] - 1
            lastIdx[c] = i
            for j in range(3):
                if lastIdx[j] != -1:
                    dp[i][j] = i - lastIdx[j]

        # Back-traverse
        lastIdx = [-1] * 3
        for i in range(len(colors)-1, -1, -1):
            c = colors[i] - 1
            lastIdx[c] = i
            for j in range(3):
                if lastIdx[j] != -1:
                    dp[i][j] = min(dp[i][j], lastIdx[j] - i)

        res = []
        for i, c in queries:
            if dp[i][c-1] == inf:
                res.append(-1)
            else:
                res.append(dp[i][c-1])
        return res
    
    
    # 2022/03/05 
    # Map + Build-in BS [O(N + Q*log(N)): 52%]
    def shortestDistanceColor2(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        print("Code2")
        ##Generate the map 
        colorToIndices = collections.defaultdict(list)
        for i, color in enumerate(colors):
            colorToIndices[color].append(i)

        res = []
        for i, c in queries:
            if len(colorToIndices[c]) == 0:
                res.append(-1)
                continue
            idx = bisect.bisect_left(colorToIndices[c], i)
            if idx == 0:
                res.append(abs(i-colorToIndices[c][0]))
            elif idx == len(colorToIndices[c]):
                res.append(abs(i-colorToIndices[c][-1]))
            else:
                diff1 = abs(i-colorToIndices[c][idx-1])
                diff2 = abs(i-colorToIndices[c][idx])
                res.append(min(diff1, diff2))
        return res
                
    # 2022/03/05
    # Map + Binary Search [O(N + Q*log(N)): 81%]
    def shortestDistanceColor1(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        print("Code1")
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