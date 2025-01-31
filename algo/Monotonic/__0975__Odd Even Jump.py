class Solution:
    
    # 2022/01/16 
    # Monotonic stack for index; sort value [O(nlogn): 50%]    
    def oddEvenJumps(self, arr: List[int]) -> int:
        print("Code3")
        
        n = len(arr)
        descStack = []
        greaterArr = [-1] * n
        
        ascStack = []
        lessArr = [-1] * n
    
        for v, i in sorted([a, i] for i, a in enumerate(arr)):
            while descStack and descStack[-1] < i :
                idx = descStack.pop()
                greaterArr[idx] = i
            descStack.append(i)
        
        for v, i in sorted([-a, i] for i, a in enumerate(arr)):
            while ascStack and ascStack[-1] < i :
                idx = ascStack.pop()
                lessArr[idx] = i
            ascStack.append(i)
        
        # print(arr)
        # print("great:", greaterArr)
        # print("less :", lessArr)
        
        higher = [False] * n
        lower = [False] * n
        higher[-1] = lower[-1] = True
        #print(higher)
        #print(lower)
        for i in range(len(arr) - 2, -1, -1):
            if greaterArr[i] != -1:
                higher[i] = lower[greaterArr[i]]
            if lessArr[i] != -1:
                lower[i] = higher[lessArr[i]] 
        #print(higher)
        #print(lower)
        return sum(higher)
    
    # =================================================
    # Reverse to find back []
    def oddEvenJumps2(self, arr: List[int]) -> int:
        print("Code2")
        arr = arr[::-1]
        goods = set([arr[0]])
        candidates = set([arr[0]])
        
        def findLarger(arr, start):
            maxVal = inf
            res = []
            for i in range(start, len(arr)):
                if arr[start] < arr[i] < maxVal:
                    maxVal = arr[i]
                    res.append(arr[i])
            return res
    
        def findSmaller(arr, start):
            minVal = -inf
            res = []
            for i in range(start, len(arr)):
                if arr[start] > arr[i] > minVal:
                    minVal = arr[i]
                    res.append(arr[i])
            return res
            
        #def findSmaller() 
        print("Larger:", findLarger(arr, 0))
        print("Smaller:", findSmaller(arr, 0))
        
    # =================================================
    # Tabluar DP [TLE]
    def oddEvenJumps1(self, arr: List[int]) -> int:
        print("Code1")
        n = len(arr)
        dp = [[None, None] for _ in range(n)] #odd, even
        
        def fillDpTable(dp, steps, result):
            for idx, mode in steps:
                dp[idx][mode] = result
        
        for start in range(n):
            cur = start
            mode = 0
            steps = [(start, mode)]
            while cur < n:
                # if dp[cur][mode] is not None:
                #     fillDpTable(dp, steps, dp[cur][mode])
                #     break
                
                if cur == n - 1: #True case
                    fillDpTable(dp, steps, True)
                    break 
                    
                if mode == 0:  #odd
                    minVal = inf
                    minIdx = -1
                    for nxt in range(cur + 1, n):
                        if arr[cur] <= arr[nxt] < minVal:
                            minIdx = nxt
                            minVal = arr[nxt]
                    if minIdx == -1:  #False case 
                        fillDpTable(dp, steps, False)
                        break
                    cur = minIdx 
                    mode = 1        
                elif mode == 1:
                    maxVal = -inf
                    maxIdx = -1
                    for nxt in range(cur + 1, n):
                        if maxVal < arr[nxt] <= arr[cur]:
                            maxIdx = nxt
                            maxVal = arr[nxt]
                    if maxIdx == -1:  #False case 
                        fillDpTable(dp, steps, False)
                        break
                    cur = maxIdx 
                    mode = 0
                steps.append((cur, mode))
                      
        count = 0 
        for i, row in enumerate(dp):
            if row[0] == True:
                count += 1
            #print(i, row, arr[i])
        return count
                        
                