class Solution:
    
    #2022/02/20
    #Greedy[O(n): 79%]
    def jump(self, nums: List[int]) -> int:
        print("Code2")
        if len(nums) <= 1:
            return 0
        dp = [inf] * len(nums)
        dp[0] = 0
        
        curIdx = 0
        nextStep = 0
        while curIdx < len(nums):
            furthestStep = 0
            for step in range(1, nums[curIdx]+1):
                nextIdx = curIdx + step
                if nextIdx >= len(nums) - 1:
                    return dp[curIdx] + 1
                if nextIdx + nums[nextIdx] > furthestStep:
                    furthestStep = nextIdx + nums[nextIdx] 
                    nextStep = nextIdx
            dp[nextStep] = dp[curIdx] + 1
            curIdx = nextStep
        return dp[-1]
            
    
    #2022/02/14
    #DP[O(n2): 5%]
    def jump1(self, nums: List[int]) -> int:
        print("Code1")
        dp = [inf] * len(nums)
        dp[0] = 0
        for i, v in enumerate(nums):
            for j in range(1, v+1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[-1]