class Solution:
    
    # 2022/02/19
    # DP [O(nlogn + n): 54%]
    def deleteAndEarn(self, nums: List[int]) -> int:
        print("Code2")
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        count = sorted(list(count.items()))
        dp = [[0] * 2 for _ in range(len(count))]
        dp[0][0] = count[0][0] * count[0][1]  #use
        dp[0][1] = 0            #not use
        for i in range(1, len(count)):
            if count[i-1][0] == count[i][0] - 1: 
                dp[i][0] =  dp[i-1][1] + count[i][0] * count[i][1]
            else:
                dp[i][0] =  max(dp[i-1][0], dp[i-1][1]) + count[i][0] * count[i][1]    
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        return max(dp[-1][0], dp[-1][1])
        
        
    # 2022/02/18   
    # Memoization DP [TLE]
    def deleteAndEarn1(self, nums: List[int]) -> int:
        print("Code1")
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        
        def dfs(count, countList, start, end, memo):
            if start >= end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            maxScore = 0
            for i in range(start, end):
                score = countList[i] * count[countList[i]]
                if i+1 < end and  countList[i+1] == countList[i] + 1:
                    score += dfs(count, countList, i+2, end, memo)
                else:
                    score += dfs(count, countList, i+1, end, memo)
                if i-1 >= start and  countList[i-1] == countList[i] - 1:
                    score += dfs(count, countList, start, i-2, memo)
                else:
                    score += dfs(count, countList, start, i-1, memo)
                maxScore = max(maxScore, score)
            memo[(start, end)] = maxScore
            return maxScore
        return dfs(count, sorted(list(count.keys())), 0, len(count), {})