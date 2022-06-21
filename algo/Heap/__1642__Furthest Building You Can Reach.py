class Solution:
    
    # 2022/06/21
    # Min-Heap (only small ones use bricks) [O(nlogn): 68% / O(n): 16%]
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        print("Code2")
        heap = [] #num of ladder used 
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                pop = heapq.heappop(heap)
                if pop <= bricks:
                    bricks -= pop
                else:
                    return i - 1
        return len(heights) - 1
            
        
    #DFS / DP [Incorrect yet] 
    def furthestBuilding1(self, heights: List[int], bricks: int, ladders: int) -> int:
        # dp(n, b, l) = dp(n-1, b, l) + 1  if v(n-1) >= v(n) 
        # dp(n, b, l) = dp(n-1, b-(v(n) - v(n-1)), l-1)  if v(n-1) < v(n)
    
        if len(heights) <= 1:
            return 0
        
        def dfs(b, l, idx):
            print(b, l, idx)
            if b < 0 or l < 0:
                return idx - 1
            if idx == len(heights):
                return idx - 1
        
            if heights[idx-1] >= heights[idx]:
                useNothing = dfs(bricks, ladders, idx + 1)
                return useNothing
            else:
                useBrick = dfs(b - (heights[idx] - heights[idx-1]), l, idx + 1)
                useLadder = dfs(b, l-1, idx + 1)
                res = max(useBrick, useLadder)
                print(" ", b, l, idx, "=>", useBrick, useLadder)
                return res
        return dfs(bricks, ladders, 1)