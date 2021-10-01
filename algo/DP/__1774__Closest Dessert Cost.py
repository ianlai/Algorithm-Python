class Solution:
    
    # Top-Down DP (Memoization)
    # Base  = N, Topping =  M
    # Time  = O(NM*Target)   //99%
    # Space = O( M*Target)   //49%
    
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        print("Top-Down DP (Memoization)")
    
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
        print("DFS")
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