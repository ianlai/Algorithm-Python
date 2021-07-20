class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        allSum = sum(nums) 
        if allSum % 2 != 0:
            return False
        target = allSum / 2 
        memo = set()
        
        return self.targetSum(nums, 0, target, memo)
        
    def targetSum(self, nums, idx, target, memo):
        if target == 0:
            return True
        if target in memo:
            return False
            #return memo[target]
        if idx >= len(nums):
            return False
        
        if self.targetSum(nums, idx + 1, target - nums[idx], memo):
            #memo[target] = True
            return True
        if self.targetSum(nums, idx + 1, target, memo):
            #memo[target] = True
            return True
        memo.add(target) 
        return False