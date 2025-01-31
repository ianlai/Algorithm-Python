class Solution:
    #def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # numsum = sum(nums)
        # maxVal = target + numsum 
        # minVal = target - numsum
        # val = target - minVal 
        # valLength = numsum * 2 + 1 
        # dp = [for i in ]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total = 0
        memo = {}
        #a = self.helper(nums, -target + nums[0], 0, memo, "+" + str(nums[0]))
        #b = self.helper(nums, -target - nums[0], 0, memo, "-" + str(nums[0]))
        return self.helper(nums, -target, -1, memo)
    
    def helper(self, nums, target, idx, memo):
        #print(target, idx, exp)
        if idx == len(nums) - 1:
            if target == 0:
                #print(">> ", exp)
                return 1 
            else:
                return 0
        if idx >= len(nums):
            return 0 
        if (target, idx) in memo:
            return memo[(target, idx)]
    
        count = 0
        #for i in range(idx+1, len(nums)):
        i = idx + 1 
        #count += self.helper(nums, target + nums[i], i , memo, exp + "+" + str(nums[i]))
        #count += self.helper(nums, target - nums[i], i , memo, exp + "-" + str(nums[i]))
        count += self.helper(nums, target + nums[i], i , memo)
        count += self.helper(nums, target - nums[i], i , memo)
        memo[(target, idx)] = count
        return count 