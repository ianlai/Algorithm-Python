class Solution:
    
    # DP + Two-size list with general Top-k func [O(n*kn), k=2: 37%]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        print("Code-5: DP + Two-size list with general top-k func")
        n = len(matrix)
        
        # Find top-k [20%]
        def push2(arr, k, value, less): 
            for idx in range(len(arr)):
                if less(value[1], arr[idx][1]):
                    arr.insert(idx, value)
                    if len(arr) > k:
                        arr = arr[:k]
                    return
            if len(arr) < k:
                arr.append(value)
        
        # Find top-k [20%]
        def push1(arr, k, val, less):
            if len(arr) == 0:
                arr.append(val)
            else:
                for i in range(len(arr)):
                    if less(val[1], arr[i][1]):
                        arr.insert(i, val)
                        if len(arr) > k:
                            arr = arr[:k]
                            #arr.pop()
                            return
                arr.append(val)
                if len(arr) > k:
                    arr.pop()
                arr = arr[:k]
        
        # Init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # DP 
        for i in range(1, n):
            # Find 1st and 2nd smallest in row i 
            arr = []
            for j in range(n): 
                push1(arr, 2, (j, dp[i-1][j]), lambda x, y: x < y)
            #print(arr)
            min1Idx, min1Val = arr[0]
            min2Idx, min2Val = arr[1]

            # Inner loop (N) 
            for j in range(n):
                if j == min1Idx:
                    minVal = min2Val
                else:
                    minVal = min1Val
                dp[i][j] = minVal + matrix[i][j]
        return min(dp[n-1])
    
    # ==============================================================
    
    # DP + Two-size queue [O(n2): 54%]
    def minFallingPathSum4(self, matrix: List[List[int]]) -> int:
        print("Code-4: DP + Two-size queue ")
        n = len(matrix)
        
        # Init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # DP 
        for i in range(1, n):
            # Find 1st and 2nd smallest in row i 
            deq = collections.deque()
            if dp[i-1][0] < dp[i-1][1]:
                deq.append((0, dp[i-1][0]))
                deq.append((1, dp[i-1][1]))
            else:
                deq.append((1, dp[i-1][1]))
                deq.append((0, dp[i-1][0]))
                
            for j in range(2, n):
                cur = (j, dp[i-1][j])
                if cur[1] < deq[0][1]:
                    deq.pop()
                    deq.appendleft(cur)
                elif cur[1] < deq[1][1]:
                    deq.pop()
                    deq.append(cur)
            
            min2Idx, min2Val = deq.pop()
            min1Idx, min1Val = deq.pop()
            
            # Inner loop (N) 
            for j in range(n):
                if j == min1Idx:
                    minVal = min2Val
                else:
                    minVal = min1Val
                dp[i][j] = minVal + matrix[i][j]
        return min(dp[n-1])
    
    # ==============================================================
    
    # DP + Record two mins [O(n2): 74%]
    def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        print("Code-3: DP + Two Mins")
        n = len(matrix)
        
        # Init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # DP 
        for i in range(1, n):
            # Find 1st and 2nd smallest in row i (3N)
            min1Val = min(dp[i-1])
            min1Idx = dp[i-1].index(min1Val)
            min2Val = inf
            if dp[i-1][:min1Idx]:
                min2Val = min(dp[i-1][:min1Idx]) 
            if dp[i-1][min1Idx+1:]:
                min2Val = min(min2Val, min(dp[i-1][min1Idx+1:]))
            
            # Inner loop (1N)
            for j in range(n):
                minVal = min1Val
                if j == min1Idx:
                    minVal = min2Val
                dp[i][j] = minVal + matrix[i][j]
        return min(dp[n-1])
    
    # ==============================================================

    
    # DP + Heap [O(n*(nlogn+n)) = O(n2*logn): 53%]
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        print("Code-2: DP + Heap")
        n = len(matrix)
        
        # init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        h1 = []
        for j in range(n):
            dp[0][j] = matrix[0][j]
            heapq.heappush(h1, (dp[0][j], j))
        
        # dp 
        for i in range(1, n):
            h2 = []
            min1, min1Idx = heapq.heappop(h1)
            min2, min2Idx = h1[0]
            heapq.heappush(h1, (min1, min1Idx))
            for j in range(n):
                if min1Idx != j:
                    minVal = min1
                else:
                    minVal = min2
                dp[i][j] = minVal + matrix[i][j]
                heapq.heappush(h2, (dp[i][j], j))
            h1 = h2
        return min(dp[n-1])
    
    # ==============================================================
    
    # DP [O(n3): 25%]
    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        print("Code-1: DP")
        n = len(matrix)
        
        # init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # dp 
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j+1:])
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][:j])
                else:
                    dp[i][j] = min(min(dp[i-1][j+1:]), min(dp[i-1][:j]))
                    
                dp[i][j] += matrix[i][j]

        return min(dp[n-1])