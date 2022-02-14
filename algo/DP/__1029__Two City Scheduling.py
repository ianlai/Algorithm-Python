class Solution:

    # ===============================================
    # Greedy [O(n): 57%]
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        print("Code2")
        diffCosts = []
        for i, cost in enumerate(costs):
            diff = cost[0] - cost[1]
            if diff >= 0:
                diffCosts.append((diff, i, True))
            else:
                diffCosts.append((-diff, i, False))
                
        diffCosts.sort(reverse=True)
        res = 0
        count0 = count1 = len(costs) //2
        for i in range(len(costs)):
            if count0 == 0:
                res += costs[diffCosts[i][1]][1]
                count1 -= 1
            elif count1 == 0:
                res += costs[diffCosts[i][1]][0]
                count0 -= 1
            else:
                if diffCosts[i][2]:
                    res += costs[diffCosts[i][1]][1]
                    count1 -= 1
                else:
                    res += costs[diffCosts[i][1]][0]
                    count0 -= 1
        return res
            
    # ===============================================
    # DP [O(n2): 5%]
    def twoCitySchedCost1(self, costs: List[List[int]]) -> int:
        print("Code1")
        n = len(costs) // 2
        dp = [ [inf for _ in range(n+1) ] for _ in range(2*n)] 
        
        dp[0][0] = costs[0][1]
        dp[0][1] = costs[0][0]
        
        for i in range(1, 2*n):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + costs[i][1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + costs[i][0], dp[i-1][j] + costs[i][1])
        return dp[2*n-1][n]