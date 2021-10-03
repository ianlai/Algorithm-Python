# https://leetcode.com/problems/closest-dessert-cost/
class Solution:
    
    # Buttom-Up DP (2 sets with pruning)
    # Base  = N, Topping =  N
    # Time  = O(M*target)   //99%
    # Space = O(M*target)   //45%
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method6: Buttom-Up DP (2 sets with pruning)")
        set1 = set(baseCosts)
        for idx, topping in enumerate(toppingCosts):
            set2 = set()
            for last in set1:
                set2.add(last)
                
                if last > target:
                    continue
                set2.add(last+topping)
                
                if last+topping > target:
                    continue
                set2.add(last+topping+topping)
            set1 = set2
                
        # Find answer in last row
        return min(set1, key = lambda x: (abs(x-target), x))
    
    # ==================================================================================

    # Buttom-Up DP (Filling in map with set)
    # Base  = N, Topping =  M
    # With pruning: 
    # Time  = O(M*target)   //98%
    # Space = O(M*target)   //50%
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method5: Buttom-Up DP (map with set)")
        dp = collections.defaultdict(set)
        
        dp[0] = set(baseCosts)
            
        for idx, topping in enumerate(toppingCosts):
            for last in dp[idx]:
                dp[idx+1].add(last)
                
                if last > target:
                    continue
                dp[idx+1].add(last+topping)
                
                if last+topping > target:
                    continue
                dp[idx+1].add(last+topping+topping)
                
                # Incorrect bounds
                # if last + topping <= target:
                # if last + topping + topping <= target:
                
        # Find answer in last row
        return min(dp[len(toppingCosts)], key = lambda x: (abs(x-target), x))
    # ==================================================================================
    
    # Buttom-Up DP (Filling in map with set)
    # Base  = N, Topping =  M
    
    # Without pruning (only duplication prevention): 
    # Time  = O(M*(sum_of_topping*2+max(base)))  //61%
    #       = O(M*3^N)  
    # Space = O(M*(sum_of_topping*2+max(base)))   //14%
    
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method4: Buttom-Up DP (map with set)")
        dp = collections.defaultdict(set)
        
        dp[0] = set(baseCosts)
            
        for idx, topping in enumerate(toppingCosts):
            for last in dp[idx]:
                dp[idx+1].add(last)
                dp[idx+1].add(last+topping)
                dp[idx+1].add(last+topping+topping)
                
        # Find answer in last row
        res = inf
        for possibleSum in dp[len(toppingCosts)]:
            if abs(possibleSum - target) < abs(res - target):
                res = possibleSum
            if abs(possibleSum - target) == abs(res - target) and possibleSum < res:
                res = possibleSum
        return res
    
    # ==================================================================================

    # Buttom-Up DP (matrix)
    # Base  = N, Topping =  M
    # Time  = O((target+N+M)*M)   //56%
    # Space = O((target+N+M)*M)   //37%
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method3: Buttom-Up DP (matrix)")

        row = len(toppingCosts) + 1 
        col = target + max(baseCosts) + max(toppingCosts)  
        dp = [[0 for _ in range(col)] for _ in range(row)]
        print("row:", row, " col:", col)
        
        for base in baseCosts:
            if base < col:
                dp[0][base] = 1
            
        for i in range(1, row):
            for j in range(col):
                if dp[i-1][j] == 1:
                    dp[i][j] = 1
                    if j + toppingCosts[i-1] < col:
                        dp[i][j + toppingCosts[i-1]] = 1 
                    if j + toppingCosts[i-1] * 2 < col:
                        dp[i][j + toppingCosts[i-1] * 2] = 1 
        
        # Find a "1" closest to target 
        for d in range(col): 
            j = target - d
            if j >= 0 and j < col and dp[-1][j] == 1:
                return j
            j = target + d  
            if j >= 0 and j < col and dp[-1][j] == 1:
                return j
            
        # Special case: "target - d" reaches 0 or "target + d" reaches col
        # We should just get a "1" with the smallest col then 
        for j in range(col):
            if dp[-1][j] == 1:
                return j
    
    # ==================================================================================
    
    # Top-Down DP (Memoization)
    # Base  = N, Topping =  M
    # Time  = O(NM*Target)   //99%
    # Space = O( M*Target)   //49%
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method2: Top-Down DP (Memoization)")
    
        def dfs(toppingCosts, target, idx, cur, memo):
            if cur >= target or idx >= len(toppingCosts):
                return cur
            if (cur, idx) in memo:
                return memo[(cur, idx)]

            sum0 = dfs(toppingCosts, target, idx+1, cur, memo)
            sum1 = dfs(toppingCosts, target, idx+1, cur+toppingCosts[idx], memo)
            sum2 = dfs(toppingCosts, target, idx+1, cur+toppingCosts[idx]*2, memo)

            closestSum = findClosest(target, [sum0, sum1, sum2])
            memo[(cur, idx)] = closestSum
            return closestSum
    
        def findClosest(target, arr):
            ans = float("inf")
            for item in arr:
                if abs(item - target) < abs(ans - target):
                    ans = item
                if abs(item - target) == abs(ans - target) and item < ans:
                    ans = item
            return ans
        
        memo = {}
        closestSum = float("inf")
        for base in baseCosts:
            curSum = dfs(toppingCosts, target, 0, base, memo)
            closestSum = findClosest(target, [curSum, closestSum])
            
        return closestSum
    
    # ==================================================================================
    
    # DFS  
    # Base  = N, Topping = M
    # Time  = O(N * 3^M)   //59%
    # Space = O(M)         //57%
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Method1: DFS")
        def dfs(toppingCosts, target, idx, cur):
            if cur >= target or idx >= len(toppingCosts):
                return cur

            sum0 = dfs(toppingCosts, target, idx+1, cur)
            sum1 = dfs(toppingCosts, target, idx+1, cur+toppingCosts[idx])
            sum2 = dfs(toppingCosts, target, idx+1, cur+toppingCosts[idx]*2)

            return findClosest(target, [sum0, sum1, sum2])
    
        def findClosest(target, arr):
            ans = float("inf")
            for item in arr:
                if abs(item - target) < abs(ans - target):
                    ans = item
                if abs(item - target) == abs(ans - target) and item < ans:
                    ans = item
            return ans
        
        closestSum = float("inf")
        for base in baseCosts:
            curSum = dfs(toppingCosts, target, 0, base)
            closestSum = findClosest(target, [curSum, closestSum])
            
        return closestSum