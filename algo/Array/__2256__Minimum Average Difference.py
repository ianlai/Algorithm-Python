class Solution:
    
    # Prefix sum [O(n): 25% / O(1): 25%]
    def minimumAverageDifference(self, nums: List[int]) -> int:        
        leftSum = 0
        rightSum = sum(nums)
        
        minAvgDiff = inf
        minAvgDiffIdx = None
        
        for i in range(len(nums)):
            leftSum += nums[i]
            rightSum -= nums[i]
            
            if i != len(nums) - 1:
                avgDiff = abs(leftSum // (i+1) - rightSum // (len(nums)-1-i)) 
            else:
                avgDiff = leftSum // (i+1)
                
            if avgDiff < minAvgDiff:
                minAvgDiff = avgDiff
                minAvgDiffIdx = i
            
        return minAvgDiffIdx