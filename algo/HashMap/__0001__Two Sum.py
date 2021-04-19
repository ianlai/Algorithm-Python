class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums is None:
            return []
        
        diffToIdx = {}
        for idx in range(len(nums)):
            if nums[idx] in diffToIdx:
                return [idx, diffToIdx[nums[idx]]]
            
            diff = target - nums[idx]
            diffToIdx[diff] = idx
        return []