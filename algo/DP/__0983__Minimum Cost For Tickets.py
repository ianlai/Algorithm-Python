class Solution:
    
    # 1D DP [O(n): 60%]
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        print("Code3")
        dp = [0] * (days[-1] + 1)
        for day in range(1, days[-1]+1):
            if day in days:
                costDay   = dp[max(day-1, 0)] + costs[0]
                costWeek  = dp[max(day-7, 0)] + costs[1]
                costMonth = dp[max(day-30, 0)] + costs[2]
                dp[day] = min(costDay, costWeek, costMonth)
            else:
                dp[day] = dp[day-1]
        return dp[days[-1]]
        
    # 2D DP [Incorrect]
    def mincostTickets2(self, days: List[int], costs: List[int]) -> int:
        print("Code2")
        passcosts = [[1], [7], [30]]
        for i, cost in enumerate(costs):
            passcosts[i].append(cost)
        
        maxDay = days[-1]
        dp = [[inf for _ in range(31)] for _ in range(maxDay+1)]
        dp[days[0]][0] = 0
        dp[days[0]][1] = costs[0]
        dp[days[0]][7] = costs[1]
        dp[days[0]][30]= costs[2]        
        for i in range(days[0], maxDay+1):
            print("day:", i)
            if i in days:
                dp[i][1] = min(dp[i][1], dp[i][0] + costs[0]) 
                dp[i][7] = min(dp[i][7], dp[i][0] + costs[1]) 
                dp[i][30] = min(dp[i][30], dp[i][0] + costs[2]) 
                
            else:
                for j in range(30):
                    if j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                
            print(dp[i])
        return dp[-1][1]
                
            
    # ==========================================
    # Memoization [Incorrect]
    def mincostTickets1(self, days: List[int], costs: List[int]) -> int:
        print("Code1")
        passcosts = [[1], [7], [30]]
        for i, cost in enumerate(costs):
            passcosts[i].append(cost)
            
        print(passcosts)
        self.min_cost = inf
        
        def dfs(days, passcosts, remaining, total_cost, date, date_idx, memo, cur):
            #print(cur, total_cost)
            
            if (remaining, total_cost, date, date_idx) in memo:
                return memo[(remaining, total_cost, date, date_idx)]
            if date == days[-1]:
                if remaining > 0:
                    return min(self.min_cost, total_cost)
                else:
                    return min(self.min_cost, total_cost + passcosts[0][0])
                return
            v1 = v2 = v3 = inf
            if date < days[date_idx]:
                v1 = dfs(days, passcosts, remaining - 1, total_cost, date + 1, date_idx, memo, cur + [(date, "no travel")])
            else:
                if remaining <= 0:
                    for day, cost in passcosts:
                        v2 = min(v2, dfs(days, passcosts, remaining -1 + day, total_cost + cost, date + 1, date_idx + 1, memo, cur + [(date, day)]))
                else:
                    v3 = dfs(days, passcosts, remaining - 1, total_cost, date + 1, date_idx + 1, memo, cur + [(date, "has ticket")])
            memo[(remaining, total_cost, date, date_idx)] = min(v1, v2, v3)  
            return min(v1, v2, v3)                

            # if idx_date == len(days) - 1:
            #     self.min_cost = min(self.min_cost, total_cost)
            #     return       
#             day_diff = days[idx_date + 1] - days[idx_date]
#             if remaining < day_diff:
#                 for day, cost in passcosts:
#                     if remaining + day < day_diff:
#                         continue
#                     dfs(days, passcosts, remaining + day - day_diff, total_cost + cost, idx_date + 1, cur + [(days[idx_date], day)])
#             else:
#                 dfs(days, passcosts, remaining - day_diff, total_cost, idx_date + 1, cur + [(days[idx_date], "x")])
                    
        memo = collections.defaultdict(int)
        return dfs(days, passcosts, 0, 0, 0, 0, memo, []) #remaining, cost, date, cur